from django import forms
from django.db import models
from colorfield.fields import ColorField
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.models import ClusterableModel
from rest_framework.fields import Field
from taggit.models import TaggedItemBase, Tag as TaggitTag
from wagtail.api import APIField
from wagtail.snippets.models import register_snippet
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

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

class CustomTagSerializer(Field):
    """Custom Tag Serializer."""

    def to_representation(self, value):
        """Loop through all the tags and return the name, slug and caption as a Dict."""
        print('Test ------')
        print(value)
        return [
            {
                "color": tag.color,
                "order": tag.order,
                "tag_id": tag.tag_id,
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
    tag = models.ForeignKey(Tag, related_name='tag', on_delete=models.CASCADE, null=True, blank=True)
    color = ColorField(default='#FFFFFF')
    order = models.CharField(max_length=250, verbose_name="Уровень", null=True, blank=True, )

    panels = [
        FieldPanel('tag'),
        FieldPanel('color'),
        FieldPanel('order'),
    ]

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context
    # content_panels = Page.content_panels + [
    #     FieldPanel('intro', classname="full")
    # ]


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
    intro = models.CharField(max_length=250, verbose_name="Вступление")
    body = RichTextField(blank=True, verbose_name="Статья")
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    color_tags = ColoredTag.objects.all()
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True, verbose_name="Категории")
    page_type = models.CharField(max_length=250, choices=page_types, default='standart', verbose_name="Тип карточки")
    page_type_hover = models.CharField(max_length=250, choices=page_types_hover, default='standart', verbose_name="Тип карточки при наведении")
    page_color = models.CharField(max_length=250, choices=page_colors, default='black', verbose_name="Цвет заголовков карточки")

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
        index.SearchField('tags'),
    ]
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Основное изображение"
    )
    animate_image = models.ImageField(null=True, blank=True, verbose_name="Дополнительное изображение (анимация)")

    api_fields = [
        APIField("title"),
        # ... other fields to turn into JSON
        APIField("color_tags", serializer=CustomTagSerializer()),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Данные карточки"),
        FieldPanel('page_type'),
        FieldPanel('page_type_hover'),
        FieldPanel('page_color'),
        FieldPanel('intro'),
        ImageChooserPanel('main_image'),
        FieldPanel('animate_image'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Галлерея изображений"),
    ]


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
        verbose_name = 'Галлерея изображений'
        verbose_name_plural = 'Галлерея изображений'

class BlogTagIndexPage(Page):

    def get_context(self, request):
        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context


