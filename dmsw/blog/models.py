import datetime
import os
import random
import textwrap
from django.utils import timezone
import requests
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from colorfield.fields import ColorField
from django import forms
from django.db import connection
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import JsonResponse
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from rest_framework.fields import Field
from wagtail.admin.edit_handlers import InlinePanel, MultiFieldPanel, StreamFieldPanel, FieldRowPanel
from wagtail.api import APIField
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm
from wagtail.core import blocks
from wagtail.core.blocks import RawHTMLBlock
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page, Orderable
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.search import index

from .blocks import ContainerBlock, ContainerNarrowBlock, ContainerWideBlock
from .snipets import *

dirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def transliterate(name):
    """
    Автор: LarsKort
    Дата: 16/07/2011; 1:05 GMT-4;
    Не претендую на "хорошесть" словарика. В моем случае и такой пойдет,
    вы всегда сможете добавить свои символы и даже слова. Только
    это нужно делать в обоих списках, иначе будет ошибка.
    """
    # Слоаврь с заменами
    slovar = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
              'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
              'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
              'ц': 'c', 'ч': 'cz', 'ш': 'sh', 'щ': 'scz', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e',
              'ю': 'u', 'я': 'ia', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
              'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
              'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H',
              'Ц': 'Ts', 'Ч': 'CZ', 'Ш': 'SH', 'Щ': 'SCH', 'Ъ': '', 'Ы': 'y', 'Ь': '', 'Э': 'E',
              'Ю': 'U', 'Я': 'YA', ',': '', '?': '', ' ': '_', '~': '', '!': '', '@': '', '#': '',
              '$': '', '%': '', '^': '', '&': '', '*': '', '(': '', ')': '', '-': '', '=': '', '+': '',
              ':': '', ';': '', '<': '', '>': '', '\'': '', '"': '', '\\': '', '/': '', '№': '',
              '[': '', ']': '', '{': '', '}': '', 'ґ': '', 'ї': '', 'є': '', 'Ґ': 'g', 'Ї': 'i',
              'Є': 'e', '—': ''}

    # Циклически заменяем все буквы в строке
    for key in slovar:
        name = name.replace(key, slovar[key])
    return name


def save_mail(to_form):
    date_time = datetime.datetime.now()
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO wagtailforms_formsubmission (form_data, page_id, submit_time) '
                   f'VALUES (\'{to_form}\', 94,\'{date_time}\')')
    rows = cursor.fetchall()


def save_image(img, text, tag):
    if img:
        pos = (10, 20)
        black = (0, 0, 0)
        white = (255, 255, 255)
        w = 1050
        h = 550
        # font = ImageFont.truetype("trebucbd.ttf", 40)
        tag_font = ImageFont.truetype(dirPath + "/static/webfonts/Montserrat-Bold.ttf", 30)
        font = ImageFont.truetype(dirPath + "/static/webfonts/Montserrat-Bold.ttf", 40)
        newsize = (w, h)
        share_bg = Image.open(dirPath + '/static/image/share_bg.jpg')
        overlay = Image.open(dirPath + '/static/image/overlay.png')
        logo = Image.open(dirPath + '/static/image/logotype_over.png')
        in_path = dirPath + '/media/' + transliterate(str(img)).replace('original_images', 'original_images/')
        out_path = dirPath + '/media/to_share_imgs/' + transliterate(str(img)).replace('original_images', '')
        try:
            photo = Image.open(in_path)
            photo = photo.convert('RGB')
            photo = photo.resize(newsize)
            photo.paste(overlay, (0, 0), overlay)
        except:
            photo = Image.open(dirPath + '/static/image/share_bg.jpg')
        photo.paste(logo, (60, 60), logo)

        # make the image editable
        drawing = ImageDraw.Draw(photo)
        drawing.text((225, 78), "#Москвастобой", font=tag_font, fill=white)
        drawing.text((400, 78), tag, font=tag_font, fill=white)
        lines = textwrap.wrap(text, width=38)
        if len(lines) > 1:
            y_text = h / 2 - (50 * len(lines) / 2) + 60
        else:
            y_text = h / 2 + 60
        for line in lines:
            width, height = font.getsize(line)
            drawing.text((64, y_text), line, font=font, fill=white)
            y_text += height + 10
        photo.save(out_path)
    else:
        print('no image')


def sort_cards(pages):
    all_pages = []
    for page in pages:
        if page.ontop:
            all_pages.append(page)
    for page in pages:
        if page.ontop is False:
            all_pages.append(page)
    pages = all_pages

    all_tags = Tags.objects.all().order_by('order_num')
    temp_cards = []
    primary = []
    cards = []
    print(all_tags)
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


def lang_choiser(locale):
    limit = Q(level=0) & Q(locale=locale)
    return limit


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
                                  verbose_name="Родительский TAG",
                                  limit_choices_to=(Q(parent_id_id__isnull=True)))

    panels = [
        MultiFieldPanel([
            FieldPanel('parent_id'),
            FieldPanel('level'),
            FieldPanel('order_num'),
            FieldPanel('name'),
        ]),
    ]

    def __str__(self):
        if self.parent_id_id:
            val = "-%s- %s" % (self.parent_id_id, self.name)
        else:
            val = "%s" % (self.name)
        return val if self.name else ''

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
    locales = [
        ('ru', 'ru'),
        ('en', 'en'),
    ]
    lang = 'ru'
    tag_id = models.ForeignKey(Tags, related_name='%(class)s_tag', on_delete=models.CASCADE, null=True,
                               blank=True, verbose_name='Тег', limit_choices_to=(Q(level=0)))
    color_title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название цвета')
    color = ColorField(default='#FFFFFF', verbose_name='Цвет')
    locale = models.CharField(max_length=250, verbose_name="Language", choices=locales, default='ru')

    panels = [
        MultiFieldPanel([
            FieldPanel('tag_id'),
            FieldPanel('color_title'),
            FieldPanel('color')
        ])]

    def __str__(self):
        if self.tag_id_id:
            val = "-%s- %s" % (self.tag_id_id, self.color_title)
        else:
            val = "%s" % (self.color_title)
        return val if self.color_title else ''

    class Meta:
        verbose_name = 'Цвет тега'
        verbose_name_plural = 'Цвета тегов'


class TagColorsEN(TagColors):
    locale = 'en'
    lang = 'en'

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
    title_colors = [
        ('white', 'Белый'),
        ('black', 'Черный'),
    ]
    locales = [
        ('ru', 'ru'),
        ('en', 'en'),
    ]
    locale = models.CharField(max_length=250, verbose_name="Language", choices=locales, default='ru')
    date = models.DateField("Post date")
    publish_date = models.DateTimeField("Время публикации", null=False,
                                        default=timezone.localtime(timezone.now() - timezone.timedelta(hours=1)))
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
                                 verbose_name="Основной тег",
                                 limit_choices_to=(Q(level=0))
                                 )
    sub_tag = models.ForeignKey('Tags', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',
                                verbose_name="Дополнительный тег",
                                limit_choices_to=(Q(parent_id_id__isnull=False)))
    main_color = models.ForeignKey('TagColors', null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name='+', verbose_name="Основной цвет", )
    color_tags = TagColors.objects.all()
    page_type = models.CharField(max_length=250, choices=page_types, default='standart', verbose_name="Тип карточки")
    page_type_hover = models.CharField(max_length=250, choices=page_types_hover, default='standart',
                                       verbose_name="Тип карточки при наведении")
    page_color = models.CharField(max_length=250, choices=page_colors, default='black',
                                  verbose_name="Цвет заголовков карточки")
    title_color = models.CharField(max_length=10, choices=title_colors, default='black',
                                   verbose_name='Цвет заголовка внутри карточки')
    title_image = models.ForeignKey('wagtailimages.Image',
                                    null=True,
                                    blank=True,
                                    on_delete=models.SET_NULL,
                                    related_name='+',
                                    verbose_name="Изображение заголовка на фон")
    show_image_on_mobile = models.BooleanField('показывать "Изображение заголовка на фон" на мобильных', default=False,
                                               null=False, blank=True)
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Основное изображение"
    )
    animate_image = models.ImageField(null=True, blank=True, verbose_name="Дополнительное изображение (анимация)")
    ontop = models.BooleanField('поднять', null=False, blank=True, default=False)
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
            FieldPanel('publish_date'),
            FieldPanel('locale'),
            FieldPanel('card_title'),
            FieldPanel('card_sub_title'),
            FieldPanel('main_tag', classname='main_tag'),
            FieldPanel('sub_tag', classname='sub_tag'),
            FieldPanel('main_color', classname='main_color'),
            FieldPanel('page_type'),
            FieldPanel('page_type_hover'),
            FieldPanel('page_color'),
            FieldPanel('adv_link'),
            FieldPanel('ontop', widget=forms.CheckboxInput),
            # FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Данные карточки"),
        MultiFieldPanel([
            FieldPanel('intro'),
            ImageChooserPanel('main_image'),
            FieldPanel('animate_image'),
        ]),
        MultiFieldPanel([
            FieldPanel('article_title'),
            ImageChooserPanel('title_image'),
            FieldPanel('show_image_on_mobile', widget=forms.CheckboxInput),
            FieldPanel('title_color'),
            ImageChooserPanel('article_image')],
            heading="Заголовок внутри карточки",
            classname="collapsible"
        ),
        StreamFieldPanel('content_body'),
        # FieldPanel('body', classname="full"),
        # InlinePanel('gallery_images', label="Галерея изображений"),
    ]

    def save(self, *args, **kwargs):
        # save_image(self.article_image, self.title)
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
        pages = BlogPage.objects.live().order_by('-date')
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
        ordering = ('page_ptr_id', '-date',)
        verbose_name = 'Статья'


# class BlogPageEN(BlogPage):
#     print('BlogPageEN')
#     locale = 'en'
#
#     def save(self, *args, **kwargs):
#         self.locale = 'en'
#         return super().save(*args, **kwargs)
#
#     class Meta:
#         verbose_name = 'Article in English'


class BlogIndexPage(Page):

    def serve(self, request):
        if "email" in request.POST:
            email = request.POST['email']

            list_id = '177645'
            url = "https://api.notisend.ru/v1/email/lists/" + list_id + "/recipients"
            payload = {'unconfirmed': '1',
                       'email': '' + email + ''}
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer 529b446badf979b0a8da0967860c8cde'
            }
            response = requests.post(url, headers=headers, json=payload, )
            if 'errors' in response.json():
                pass
                # print(response.json()['errors'][0]['detail'])
            else:
                # print(response.json())
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
        context = super().get_context(request)
        posts = BlogIndexPage.get_children(self).specific().live().order_by('-blogpage__date')
        blogpages = []
        for post in posts:
            if timezone.localtime(timezone.now()) > post.publish_date:
                blogpages.append(post)
        search_query = request.GET.get('q', None)
        if search_query == '':
            search_query = None
        if search_query:
            blogpages = []
            posts = BlogIndexPage.get_children(self).specific().live().order_by('-blogpage__date')
            for post in posts:
                if search_query.lower() in post.search_body or search_query.lower() in post.title:
                    blogpages.append(post)
        cards = sort_cards(blogpages)
        # print(cards)
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

    def child_pages(self):
        return BlogIndexPageEN.get_children(self).specific().order_by('-first_published_at')

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        posts = BlogIndexPage.get_children(self).specific().live().order_by('-blogpage__date')
        blogpages = []
        for post in posts:
            if timezone.localtime(timezone.now()) > post.publish_date:
                blogpages.append(post)
        search_query = request.GET.get('q', None)
        if search_query == '':
            search_query = None
        if search_query:
            blogpages = []
            posts = BlogIndexPage.get_children(self).specific().live().order_by('-blogpage__date')
            for post in posts:
                if search_query.lower() in post.search_body or search_query.lower() in post.title:
                    blogpages.append(post)
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
        blogpages = BlogPage.objects.all().order_by('-first_published_at')
        search_query = request.GET.get('q', None)
        if search_query == '':
            search_query = None
        if search_query:
            blogpages = BlogPage.objects.all().order_by('-first_published_at').search(search_query)
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
            blogpages = BlogPage.objects.live().order_by('-first_published_at').filter(
                (Q(main_tag_id=tag_id) | Q(sub_tag_id=tag_id)))
        else:
            tags = []
            tag_id = Tags.objects.filter(name=tag).values('id')[0]['id']
            tags.append(tag_id)
            for tag in Tags.objects.filter(parent_id_id=tag_id).values():
                tags.append(tag['id'])
            if len(tags) > 1:
                blogpages = BlogPage.objects.live().order_by('-first_published_at').filter(
                    (Q(main_tag_id=tag_id) | Q(sub_tag_id=tag_id)))
            else:
                tag_id = int(tags[0])
                blogpages = BlogPage.objects.live().order_by('-first_published_at').filter(
                    (Q(main_tag_id=tag_id) | Q(sub_tag_id=tag_id)))
        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        context['tag'] = request.GET.get('tag')

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
    locales = [
        ('ru', 'ru'),
        ('en', 'en'),
    ]

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

    locale = models.CharField(max_length=250, verbose_name="Language", choices=locales, default='ru')
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
            FieldPanel('locale'),
            ImageChooserPanel('main_image')
        ], heading="Данные страницы"),
        StreamFieldPanel('content_body'),
        InlinePanel('typed_gallery_images', label="Партнеры"),
    ]

    class Meta:
        verbose_name = "Typed page (don't use or modify)"


class TypedPageEN(TypedPage):
    locale = 'en'

    def save(self, *args, **kwargs):
        self.locale = 'en'
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Typed page in english (don't use or modify)"


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
        ordering = ('sort_order',)


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


@receiver(post_save, sender=BlogPage)
def my_handler(sender, **kwargs):
    if BlogPage.objects.get(id=kwargs.get('instance').id).article_image:
        img = BlogPage.objects.get(id=kwargs.get('instance').id).article_image.file
    elif BlogPage.objects.get(id=kwargs.get('instance').id).main_image:
        img = BlogPage.objects.get(id=kwargs.get('instance').id).main_image.file
    else:
        img = None
    if img:
        text = BlogPage.objects.get(id=kwargs.get('instance').id).title
        tag = ''
        # if BlogPage.objects.get(id=kwargs.get('instance').id).sub_tag:
        #     tag = BlogPage.objects.get(id=kwargs.get('instance').id).sub_tag
        # else:
        #     tag = BlogPage.objects.get(id=kwargs.get('instance').id).main_tag
        save_image(img, text, tag)
