from django.db import models
from colorfield.fields import ColorField
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.models import ClusterableModel
from rest_framework.fields import Field
from wagtail.api import APIField
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm
from wagtail.core.blocks import RawHTMLBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel, FieldRowPanel
from wagtail.search import index
from django.db import connection
from .blocks import ContainerBlock, ContainerNarrowBlock, ContainerWideBlock
import datetime
import random
import requests
import os
from .snipets import *
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

dirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def save_mail(to_form):
    date_time = datetime.datetime.now()
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO wagtailforms_formsubmission (form_data, page_id, submit_time) '
                   f'VALUES (\'{to_form}\', 94,\'{date_time}\')')
    rows = cursor.fetchall()


def save_image(img, text):
    pos = (10, 20)
    black = (3, 3, 3)
    font = ImageFont.load_default()
    unicode_text = "Test text"
        #truetype(dirPath + "/statis/webfonts/ALSGorizont-ExtraBoldExpanded.ttf", 40)
    in_path = dirPath + '/media/original_images/' + str(img)
    out_path = dirPath + '/media/to_share_imgs/' + str(img)
    print(in_path, out_path, text)
    photo = Image.open(in_path)
    # make the image editable
    drawing = ImageDraw.Draw(photo)
    drawing.text(pos, unicode_text, fill=black, font=font)
    photo.save(out_path)

def sort_cards(pages):
    all_tags = Tags.objects.all()
    temp_cards = []
    primary = []
    cards = []
    for tag in all_tags:
        if tag.level == 0:
            primary.append(tag.id)
    card_tags = dict.fromkeys(primary)
    for el in card_tags:
        arr = []
        for tag in all_tags:
            if tag.level != 0 and el == tag.parent_id_id:
                arr.append(tag.id)
        card_tags[el] = arr
    for page in pages:
        temp_cards.append(page)
    idx = 1

    def append(i):
        for page in temp_cards:
            if page.main_tag:
                if page.main_tag.id == i:
                    return page
            else:
                return page

    for i in range(len(temp_cards)):
        for item in card_tags:
            if idx == 4:
                p = append(1)
                if p:
                    cards.append(p)
                    temp_cards.remove(p)
                p = append(item)
                idx += 1
            else:
                p = append(item)
            if p:
                cards.append(p)
                temp_cards.remove(p)
                idx += 1
        for item in card_tags:
            for el in card_tags[item]:
                if idx == 4:
                    p = append(1)
                    idx += 1
                else:
                    p = append(el)
                if p:
                    cards.append(p)
                    temp_cards.remove(p)
                    idx += 1
    return cards


class CustomTagSerializer(Field):
    """Custom Tag Serializer."""

    def to_representation(self, value):
        """Loop through all the tags and return the name, slug and caption as a Dict."""
        return [
            {
                "color": tag.color,
                "level": tag.level,
                "tag_id": tag.tag_id,
                "name": tag.name,
                "order_num": tag.order_num,
            }
            for tag in value.all()
        ]


class Tags(ClusterableModel):
    orders_list = [
        (0, 'Главное меню'),
        (1, 'под меню'),
        (2, 'тег'),
    ]
    locales = [
        ('ru', 'ru'),
        ('en', 'en'),
    ]
    lang = 'ru'
    locale = models.CharField(max_length=250, verbose_name="Language", choices=locales, default='ru')
    name = models.CharField(max_length=250, verbose_name="Название", null=False, blank=False)
    level = models.IntegerField(choices=orders_list, default=1, null=False, blank=False, verbose_name="Уровень меню", )
    order_num = models.IntegerField(null=True, blank=True, verbose_name='Порядок')
    parent_id = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE,
                                  verbose_name="Родительский TAG", )

    # def __init__(self, *args, **kwargs):
    #     super(Tags, self).__init__(*args, **kwargs)
    #     if self.lang == 'ru':
    #         self.parent_id.queryset = Tags.objects.filter(locale='ru')
    #     elif self.lang == 'en':
    #         self.parent_id.queryset = Tags.objects.filter(locale='en')

    panels = [
        MultiFieldPanel([
            FieldPanel('parent_id'),
            FieldPanel('level'),
            FieldPanel('order_num'),
            FieldPanel('name'),
        ]),
    ]

    def __str__(self):
        return str(self.name) if self.name else ''

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class TagsEN(Tags):
    locale = 'en'
    lang = 'en'

    def save(self, *args, **kwargs):
        self.locale = 'en'
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class TagColors(models.Model):
    tag_id = models.ForeignKey(Tags, related_name='%(class)s_tag', on_delete=models.CASCADE, null=True,
                               blank=True, verbose_name='Тег', limit_choices_to={'level': 0})
    color_title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название цвета')
    color = ColorField(default='#FFFFFF', verbose_name='Цвет')

    panels = [
        MultiFieldPanel([
            FieldPanel('tag_id'),
            FieldPanel('color_title'),
            FieldPanel('color')
        ])]

    def __str__(self):
        return str(self.color_title) if self.color_title else ''

    class Meta:
        verbose_name = 'Цвет тега'
        verbose_name_plural = 'Цвета тегов'


class TagColorsEN(TagColors):
    locale = 'en'

    def save(self, *args, **kwargs):
        self.locale = 'en'
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Tag color'
        verbose_name_plural = 'Tag colors'


class BlogPage(Page):
    page_types = [
        ('standart', 'Стандарт'),
        ('fullimage', 'Заливка картинкой'),
        ('video', 'Заливка анимации'),
        ('rekcard', 'Рекламный блок'),
    ]
    page_types_hover = [
        ('standart', 'Стандарт'),
        ('fullimage', 'Заливка картинкой'),
        ('video', 'Заливка анимации'),
        ('rekcard', 'Рекламный блок'),
    ]
    page_colors = [
        ('white', 'Белый'),
        ('black', 'Черный'),
    ]
    locales = [
        ('ru', 'ru'),
        ('en', 'en'),
    ]
    locale = models.CharField(max_length=250, verbose_name="Language", choices=locales, default='ru')
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250, verbose_name="Тект ховера карточки")
    adv_link = models.CharField(max_length=250, null=True, blank=True, verbose_name="Ссылка на рекламодателя")
    body = RichTextField(blank=True, verbose_name="Вступление статьи")
    card_title = models.CharField(max_length=250, verbose_name="Заголовок карточки", blank=True)
    card_sub_title = models.CharField(max_length=250, verbose_name="Подголовок карточки", blank=True)
    hr = blocks.RichTextBlock(features=['hr'], classname='container', blank=True)
    content_body = StreamField([
        ('container', ContainerBlock()),
        ('container_narrow', ContainerNarrowBlock()),
        ('container_wide', ContainerWideBlock()),
    ], null=True, blank=True, verbose_name="Статья")
    main_tag = models.ForeignKey('Tags', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',
                                 limit_choices_to={'parent_id_id__isnull': True}, verbose_name="Основной тег")
    sub_tag = models.ForeignKey('Tags', null=True, blank=True, on_delete=models.SET_NULL,
                                limit_choices_to={'parent_id_id__isnull': False}, related_name='+',
                                verbose_name="Дополнительный тег")
    main_color = models.ForeignKey('TagColors', null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name='+', verbose_name="Основной цвет")
    color_tags = TagColors.objects.all()
    page_type = models.CharField(max_length=250, choices=page_types, default='standart', verbose_name="Тип карточки")
    page_type_hover = models.CharField(max_length=250, choices=page_types_hover, default='standart',
                                       verbose_name="Тип карточки при наведении")
    page_color = models.CharField(max_length=250, choices=page_colors, default='black',
                                  verbose_name="Цвет заголовков карточки")

    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Основное изображение"
    )
    animate_image = models.ImageField(null=True, blank=True, verbose_name="Дополнительное изображение (анимация)")
    ontop = models.BooleanField(null=True, blank=True, default=False)
    article_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Изображение для статьи"
    )
    article_title = models.TextField(max_length=200, null=True, blank=True, verbose_name="Заголовок для статьи")
    search_body = models.TextField(null=True, blank=True)

    api_fields = [
        APIField("title"),
        APIField("article_title"),
        # ... other fields to turn into JSON
        APIField("color_tags", serializer=CustomTagSerializer()),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('card_title'),
        index.SearchField('card_sub_title'),
        index.SearchField('intro'),
        index.SearchField('article_title'),
        # index.SearchField('tags'),
        # index.RelatedFields('tags', [
        #     index.SearchField('name'),
        # ]),
        index.SearchField('search_body'),
        # index.SearchField('main_tag'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('card_title'),
            FieldPanel('card_sub_title'),
            FieldPanel('main_tag'),
            FieldPanel('sub_tag'),
            FieldPanel('main_color'),
            FieldPanel('page_type'),
            FieldPanel('page_type_hover'),
            FieldPanel('page_color'),
            FieldPanel('adv_link'),
            # FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Данные карточки"),
        MultiFieldPanel([
            FieldPanel('intro'),
            ImageChooserPanel('main_image'),
            FieldPanel('animate_image'),
        ]),
        FieldPanel('article_title'),
        # FieldPanel('ontop', widget=forms.CheckboxInput),
        ImageChooserPanel('article_image'),
        StreamFieldPanel('content_body'),
        # FieldPanel('body', classname="full"),
        # InlinePanel('gallery_images', label="Галерея изображений"),
    ]

    def save(self, *args, **kwargs):
        save_image(self.article_image, self.title)
        if self.content_body.stream_data:
            self.search_body = str(self.content_body.stream_data).lower()
        return super().save(*args, **kwargs)

    def serve(self, request):
        if "email" in request.POST:

            email = request.POST['email']
            to_form = '{"email": "' + email + '"}'
            save_mail(to_form)
            data = {
                'message': "Спасибо!"
            }
            return JsonResponse(data)
        elif "ajax_load_more" in request.POST:
            more_data = {
                'message': "Загрузка ..."
            }
            return JsonResponse(more_data)
        else:
            # Display event page as usual
            return super().serve(request)

    def get_context(self, request):
        # Filter by tag
        blogpages = []
        pages = BlogPage.objects.order_by('-last_published_at').all()
        for page in pages:
            if page.sub_tag == self.sub_tag:
                blogpages.append(page)
        if len(blogpages) < 6:
            for page in pages:
                if page.main_tag == self.main_tag and page.main_tag is not None:
                    blogpages.append(page)
        random.shuffle(blogpages)
        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages

        return context

    class Meta:
        ordering = ('date',)
        verbose_name = 'Статья на Русском'


class BlogPageEN(BlogPage):
    locale = 'en'

    def save(self, *args, **kwargs):
        self.locale = 'en'
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Article in English'


class BlogIndexPage(Page):

    def serve(self, request):
        if "email" in request.POST:
            email = request.POST['email']

            list_id = '176059'
            url = "https://api.notisend.ru/v1/email/lists/" + list_id + "/recipients"
            payload = {'unconfirmed': '1',
                       'email': '' + email + ''}
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer fefb77c131fff95404fbf9537e4d6c8f'
            }
            response = requests.post(url, headers=headers, json=payload, )
            if 'errors' in response.json():
                print(response.json()['errors'][0]['detail'])
            else:
                print(response.json())
                to_form = '{"email": "' + email + '"}'
                save_mail(to_form)
                if 'en.' in request.get_host:
                    data = {
                        'message': "Thank you!"
                    }
                else:
                    data = {
                        'message': "Спасибо!"
                    }
                return JsonResponse(data)
        elif "ajax_load_more" in request.POST:
            more_data = {
                'message': "Загрузка ..."
            }
            return JsonResponse(more_data)
        else:
            # Display event page as usual
            return super().serve(request)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)

        blogpages = BlogPage.objects.live().filter(locale='ru').order_by('-last_published_at')
        search_query = request.GET.get('q', None)
        if search_query == '':
            search_query = None
        if search_query:
            blogpages = BlogPage.objects.live().order_by('-last_published_at').search(search_query.lower())
        cards = sort_cards(blogpages)
        context['locale'] = 'ru'
        context['blogpages'] = cards
        context['search_query'] = search_query
        context['entry_list'] = cards
        context['subscribe_count'] = random.randint(7, 11)
        context['page_template'] = 'blog/ajax_blog_index_page.html'

        return context

    def get_template(self, request):
        if request.is_ajax():
            # Template to render objects retrieved via Ajax
            return 'blog/ajax_blog_index_page.html'
        else:
            # Original template
            return 'blog/blog_index_page.html'

    class Meta:
        verbose_name = "Главная странице карточек (не используйте и не меняйте)"


class BlogIndexPageEN(Page):
    def serve(self, request):
        if "email" in request.POST:
            email = request.POST['email']

            list_id = '176059'
            url = "https://api.notisend.ru/v1/email/lists/" + list_id + "/recipients"
            payload = {'unconfirmed': '1',
                       'email': '' + email + ''}
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer fefb77c131fff95404fbf9537e4d6c8f'
            }
            response = requests.post(url, headers=headers, json=payload, )
            if 'errors' in response.json():
                print(response.json()['errors'][0]['detail'])
            else:
                print(response.json())
                to_form = '{"email": "' + email + '"}'
                save_mail(to_form)
                data = {
                    'message': "Спасибо!"
                }
                return JsonResponse(data)
        elif "ajax_load_more" in request.POST:
            more_data = {
                'message': "Загрузка ..."
            }
            return JsonResponse(more_data)
        else:
            # Display event page as usual
            return super().serve(request)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = BlogPage.objects.live().filter(locale='en').order_by('-last_published_at')
        search_query = request.GET.get('q', None)
        if search_query == '':
            search_query = None
        if search_query:
            blogpages = BlogPage.objects.live().order_by('-last_published_at').search(search_query.lower())
        cards = sort_cards(blogpages)
        context['locale'] = 'en'
        context['blogpages'] = cards
        context['search_query'] = search_query
        context['entry_list'] = cards
        context['subscribe_count'] = random.randint(7, 11)
        context['page_template'] = 'blog/ajax_blog_index_page.html'

        return context

    def get_template(self, request):
        if request.is_ajax():
            # Template to render objects retrieved via Ajax
            return 'blog/ajax_blog_index_page.html'
        else:
            # Original template
            return 'blog/blog_index_page.html'

    class Meta:
        verbose_name = "Main cards page in English (don't use or modify)"


class BlogPreviewPage(Page):

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = BlogPage.objects.all().order_by('-last_published_at')
        search_query = request.GET.get('q', None)
        if search_query == '':
            search_query = None
        if search_query:
            blogpages = BlogPage.objects.all().order_by('-last_published_at').search(search_query)
        cards = sort_cards(blogpages)
        context['blogpages'] = cards
        context['search_query'] = search_query
        return context

    class Meta:
        verbose_name = 'Старинца превью на русском'


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

    class Meta:
        verbose_name = 'Галерея изображений'
        verbose_name_plural = 'Галерея изображений'


class BlogTagIndexPage(Page):

    def serve(self, request):
        if "email" in request.POST:

            email = request.POST['email']
            to_form = '{"email": "' + email + '"}'
            save_mail(to_form)
            data = {
                'message': "Спасибо!"
            }
            return JsonResponse(data)
        elif "ajax_load_more" in request.POST:
            more_data = {
                'message': "Загрузка ..."
            }
            return JsonResponse(more_data)
        else:
            # Display event page as usual
            return super().serve(request)

    def get_context(self, request):
        # Filter by tag
        tag = request.GET.get('tag')
        if Tags.objects.filter(name=tag).values('parent_id_id')[0]['parent_id_id']:
            tag_id = Tags.objects.filter(name=tag).values('id')[0]['id']
            blogpages = BlogPage.objects.order_by('-last_published_at').filter(
                Q(main_tag_id=tag_id) | Q(sub_tag_id=tag_id))
        else:
            tags = []
            tag_id = Tags.objects.filter(name=tag).values('id')[0]['id']
            tags.append(tag_id)
            for tag in Tags.objects.filter(parent_id_id=tag_id).values():
                tags.append(tag['id'])
            if len(tags) > 1:
                blogpages = BlogPage.objects.order_by('-last_published_at').filter(
                    Q(main_tag_id__in=tags) | Q(sub_tag_id__in=tags))
            else:
                tag_id = int(tags[0])
                blogpages = BlogPage.objects.order_by('-last_published_at').filter(
                    Q(main_tag_id=tag_id) | Q(sub_tag_id=tag_id))
        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages

        return context

    class Meta:
        verbose_name = "Старница тегов (не используйте и не меняйте)"


class SearchPage(Page):
    def get_context(self, request):
        context = super().get_context(request)
        blogpages = BlogPage.objects.all()

        context['blogpages'] = blogpages
        return context

    class Meta:
        verbose_name = "Search page (don't use or modify)"


class TypedPage(Page):

    def serve(self, request):
        if "email" in request.POST:

            email = request.POST['email']
            to_form = '{"email": "' + email + '"}'
            save_mail(to_form)
            data = {
                'message': "Спасибо!"
            }
            return JsonResponse(data)
        elif "ajax_load_more" in request.POST:
            more_data = {
                'message': "Загрузка ..."
            }
            return JsonResponse(more_data)
        else:
            # Display event page as usual
            return super().serve(request)

    tags = Page.objects.raw('SELECT * FROM blog_tags WHERE "level" = 0')
    date = models.DateField("Post date")
    text = blocks.RichTextBlock(features=['h2', 'h3', 'bold', 'italic', 'link'], blank=True)
    hr = blocks.RichTextBlock(features=['hr'], blank=True)
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Основное изображение"
    )
    content_body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('html', RawHTMLBlock()),
        ('video', EmbedBlock()),
        ('text', text),
        ('hr', hr),
    ], null=True, blank=True, verbose_name="Статья")

    api_fields = [
        APIField("title"),
        # ... other fields to turn into JSON
        APIField("tags", serializer=CustomTagSerializer()),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('title'),
            ImageChooserPanel('main_image')
        ], heading="Данные страницы"),
        StreamFieldPanel('content_body'),
        InlinePanel('typed_gallery_images', label="Партнеры"),
    ]

    class Meta:
        verbose_name = "Typed page (don't use or modify)"


class TypedPageGalleryImage(Orderable):
    page = ParentalKey(TypedPage, on_delete=models.CASCADE, related_name='typed_gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250, verbose_name='подзаголовок')
    link = models.CharField(blank=True, max_length=250, verbose_name='ссылка')
    main_tag = models.ForeignKey('Tags', null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL,
                                 related_name='+',
                                 verbose_name="Основной тег")

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
        FieldPanel('link'),
        FieldPanel('main_tag'),
    ]

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнера'


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')

    class Meta:
        verbose_name = "Form field (don't use or modify)"


class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    class Meta:
        verbose_name = "Form page (don't use or modify)"
