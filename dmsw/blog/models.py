from django import forms
from django.db import models
from colorfield.fields import ColorField
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.models import ClusterableModel
from rest_framework.fields import Field
from taggit.models import TaggedItemBase, Tag as TaggitTag
from wagtail.api import APIField
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.blocks import RawHTMLBlock, BooleanBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.snippets.models import register_snippet
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from django.db import connection
from collections import namedtuple


@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'категории'


class AllTag():

    def GetAllTag(self):
        cursor = connection.cursor()
        cursor.execute(
            'SELECT tt.id, bc.order_num, bc.parent_id_id, bc."order", tt.name, bc.name title, bc.color FROM taggit_tag tt LEFT JOIN blog_coloredtag bc ON tt.id = bc.tag_id GROUP BY tt.id ORDER BY bc.order_num')
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        rows = [nt_result(*row) for row in cursor.fetchall()]
        return rows


class CustomTagSerializer(Field):
    """Custom Tag Serializer."""

    def to_representation(self, value):
        """Loop through all the tags and return the name, slug and caption as a Dict."""
        return [
            {
                "color": tag.color,
                "order": tag.order,
                "tag_id": tag.tag_id,
                "name": tag.name,
                "order_num": tag.order_num,
            }
            for tag in value.all()
        ]


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class ColoredTag(ClusterableModel):
    orders_list = [
        (0, 'Главное меню'),
        (1, 'под меню'),
    ]
    tag = models.ForeignKey(Tag, related_name='tag', on_delete=models.CASCADE, null=True, blank=True,)
    name = models.CharField(max_length=250, verbose_name="Название", null=False, blank=False)
    color = ColorField(default='#FFFFFF')
    order = models.IntegerField(choices=orders_list, default=1, null=False, blank=False, verbose_name="Уровень меню", )
    order_num = models.IntegerField(null=True, blank=True, verbose_name='Порядок')
    parent_id = models.ForeignKey('tag', blank=True, null=True, on_delete=models.CASCADE,
                                  verbose_name="Родительский TAG", )

    panels = [
        MultiFieldPanel([
            FieldPanel('parent_id'),
            FieldPanel('order'),
            FieldPanel('order_num'),
            FieldPanel('name'),
            FieldPanel('tag'),
            FieldPanel('color'),
        ]),
    ]

    def __str__(self):
        return str(self.name) if self.name else ''

    def __unicode__(self):
        return self.color

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class TagColors(models.Model):
    tag_id = models.ForeignKey(ColoredTag, related_name='%(class)s_tag', on_delete=models.CASCADE, null=True,
                               blank=True, verbose_name='Тег', limit_choices_to={'order': 0})
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


class BlogIndexPage(RoutablePageMixin, Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        cards = []
        temp_cards = []
        primary = []
        all_tags = AllTag().GetAllTag()
        for tag in all_tags:
            if tag.order == 0:
                primary.append(tag.id)
        card_tags = dict.fromkeys(primary)
        for el in card_tags:
            arr = []
            for tag in all_tags:
                if tag.order != 0 and el == tag.parent_id_id:
                    arr.append(tag.id)
            card_tags[el] = arr
        print(card_tags)
        blogpages = BlogPage.objects.live().order_by('-last_published_at')
        search_query = request.GET.get('q', None)
        if search_query == '':
            search_query = None
        if search_query:
            blogpages = BlogPage.objects.all().order_by('-last_published_at').search(search_query)
        for page in blogpages:
            temp_cards.append(page)
        idx = 1

        def append(i):
            for page in temp_cards:
                if page.main_tag.id == i:
                    return page

        for i in range(len(temp_cards)):
            for item in card_tags:
                if idx == 4:
                    p = append(14)
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
                        p = append(14)
                        idx += 1
                    else:
                        p = append(el)
                    if p:
                        cards.append(p)
                        temp_cards.remove(p)
                        idx += 1
        for page in cards:
            for item in card_tags:
                if page.main_tag.id == item:
                    pass
                for el in card_tags[item]:
                    if page.main_tag.id == el:
                        pass
        context['blogpages'] = cards
        context['search_query'] = search_query
        context['primary'] = primary
        context['all_tags'] = all_tags
        context['card_tags'] = card_tags
        return context


class GalleryBlock(blocks.StreamBlock):
    image = ImageChooserBlock()

    class Meta:
        template = 'blog/blocks/gallery_block.html'


class VideoBlock(blocks.StreamBlock):
    video = EmbedBlock()

    class Meta:
        template = 'blog/blocks/video_block.html'


class VideoItem(blocks.StreamBlock):
    add_video = RawHTMLBlock()

    class Meta:
        template = 'blog/blocks/video_item.html'


class ColumnBlock(blocks.StreamBlock):
    paragraph = blocks.RichTextBlock()
    image = ImageChooserBlock()
    video = VideoBlock(icon='placeholder', label='Видер блок', null=True, blank=True, required=False)
    yt_video = VideoItem(icon='placeholder', label='Видер по id', null=True, blank=True, required=False)
    html = blocks.RawHTMLBlock()
    gallery = GalleryBlock(icon='image', label='Галерея', null=True, blank=True, required=False)

    class Meta:
        template = 'blog/blocks/column_block.html'


class TwoColumnBlock(blocks.StructBlock):
    left_column = ColumnBlock(icon='arrow-right', label='Left column content', null=True, blank=True, required=False)
    right_column = ColumnBlock(icon='arrow-right', label='Right column content', null=True, blank=True, required=False)

    class Meta:
        template = 'blog/blocks/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'


class ContainerBlock(blocks.StructBlock):
    onecol = ColumnBlock(icon='cog', label='Одна колонка', null=True, blank=True, required=False)
    twocol = TwoColumnBlock(icon='cog', label='Две колонки', null=True, blank=True, required=False)

    class Meta:
        template = 'blog/blocks/container_block.html'
        icon = 'placeholder'
        label = 'Стандартный блок'


class ContainerNarrowBlock(blocks.StructBlock):
    onecol = ColumnBlock(icon='cog', label='Одна колонка', null=True, blank=True, required=False)
    twocol = TwoColumnBlock(icon='cog', label='Две колонки', null=True, blank=True, required=False)

    class Meta:
        template = 'blog/blocks/container_narrow_block.html'
        icon = 'placeholder'
        label = 'Узкий блок'


class ContainerWideBlock(blocks.StructBlock):
    onecol = ColumnBlock(icon='cog', label='Одна колонка', null=True, blank=True, required=False)
    twocol = TwoColumnBlock(icon='cog', label='Две колонки', null=True, blank=True, required=False)

    class Meta:
        template = 'blog/blocks/container_wide_block.html'
        icon = 'placeholder'
        label = 'Широкий блок'


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
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250, verbose_name="Тект ховера карточки")
    adv_link = models.CharField(max_length=250, null=True, blank=True, verbose_name="Ссылка на рекламодателя")
    body = RichTextField(blank=True, verbose_name="Вступление статьи")
    card_title = models.CharField(max_length=16, verbose_name="Заголовок карточки", blank=True)
    card_sub_title = models.CharField(max_length=16, verbose_name="Подголовок карточки", blank=True)
    hr = blocks.RichTextBlock(features=['hr'], classname='container', blank=True)
    content_body = StreamField([
        ('container', ContainerBlock()),
        ('container_narrow', ContainerNarrowBlock()),
        ('container_wide', ContainerWideBlock()),
    ], null=True, blank=True, verbose_name="Статья")
    # main_tag = BlogPageTag.objects.raw('SELECT tt.id, tt.name, bc.color FROM blog_coloredtag bc '
    #                                   'LEFT JOIN taggit_tag tt ON tt.id = bc.tag_id WHERE bc."order" = 0')
    main_tag = models.ForeignKey('Tag', null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL,
                                 related_name='+',
                                 verbose_name="Основной тег")
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True, verbose_name="Дополнительные теги")
    main_color = models.ForeignKey('TagColors', null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   related_name='+',
                                   verbose_name="Основной цвет")
    color_tags = TagColors.objects.all()
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True, verbose_name="Категории")
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
    artical_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Изображение для статьи"
    )

    artical_title = models.TextField(max_length=200, null=True, blank=True, verbose_name="Заголовок для статьи")

    api_fields = [
        APIField("title"),
        APIField("artical_title"),
        # ... other fields to turn into JSON
        APIField("color_tags", serializer=CustomTagSerializer()),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('artical_title'),
        # index.SearchField('tags'),
        index.SearchField('content_body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('card_title'),
            FieldPanel('card_sub_title'),
            FieldPanel('main_tag'),
            FieldPanel('tags'),
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
        FieldPanel('artical_title'),
        FieldPanel('ontop', widget=forms.CheckboxInput),
        ImageChooserPanel('artical_image'),
        StreamFieldPanel('content_body'),
        # FieldPanel('body', classname="full"),
        # InlinePanel('gallery_images', label="Галерея изображений"),
    ]

    def get_context(self, request):
        # Filter by tag
        tag = self.main_tag
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages

        return context

    class Meta:
        ordering = ('date',)


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

    def get_context(self, request):
        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages

        return context


class SearchPage(Page):
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        # blogpages = self.get_children().live().order_by('-last_published_at')
        blogpages = BlogPage.objects.all()
        all_tags = AllTag().GetAllTag()

        context['blogpages'] = blogpages
        return context


class TypedPage(Page):
    # tags = RawSQL('SELECT * FROM blog_coloredtag WHERE "order" = %s', (0,))
    tags = Page.objects.raw('SELECT * FROM blog_coloredtag WHERE "order" = 0')
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


class TypedPageGalleryImage(Orderable):
    page = ParentalKey(TypedPage, on_delete=models.CASCADE, related_name='typed_gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250, verbose_name='подзаголовок')
    link = models.CharField(blank=True, max_length=250, verbose_name='ссылка')
    main_tag = models.ForeignKey('Tag', null=True,
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
