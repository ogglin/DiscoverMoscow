from colorfield.fields import ColorField
from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.core import blocks
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.fields import RichTextField, StreamField

class Sliders(models.Model):
    slider_types = [
        ('standart', 'Стандарт'),
        ('calendar', 'Календарь'),
    ]
    color = ColorField(default='#FFFFFF', verbose_name="цвет")
    title = models.CharField(max_length=128, null=True, blank=True, verbose_name="заголовок")
    subtitle = models.CharField(blank=True, max_length=250, verbose_name="подзаголовок")
    standart_link = models.CharField(blank=True, max_length=255, verbose_name="ссылка")
    image = models.ForeignKey(
        'wagtailimages.Image', blank=True, null=True, on_delete=models.CASCADE, related_name='+'
    )
    slider_type = models.CharField(max_length=250, choices=slider_types, default='black', verbose_name="Тип слайда")
    title_one = models.CharField(max_length=250, blank=True, verbose_name="подзаголовок 1")
    tag_link_one = models.CharField(blank=True, max_length=255, verbose_name="ссылка 1")
    title_two = models.CharField(max_length=250, blank=True, verbose_name="подзаголовок 2")
    tag_link_two = models.CharField(blank=True, max_length=255, verbose_name="ссылка 2")
    title_three = models.CharField(max_length=250, blank=True, verbose_name="подзаголовок 3")
    tag_link_three = models.CharField(blank=True, max_length=255, verbose_name="ссылка 3")
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('slider_type'),
            FieldPanel('title'),
            FieldPanel('subtitle'),
            FieldPanel('color'),
            FieldPanel('standart_link'),
        ], heading="Данные слайдера"),
        ImageChooserPanel('image'),
        MultiFieldPanel([
            FieldPanel('title_one'),
            FieldPanel('tag_link_one'),
            FieldPanel('title_two'),
            FieldPanel('tag_link_two'),
            FieldPanel('title_three'),
            FieldPanel('tag_link_three'),
        ], heading="Данные календаря"),
    ]

    class Meta:
        verbose_name = 'Изображение слайдера'
        verbose_name_plural = 'Изображения слайдера'
