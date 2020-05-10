import os
from colorfield.fields import ColorField
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from blog.models import Tag


# Create your models here.

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
    collect = models.CharField(blank=True, max_length=255, verbose_name="название подборки")
    collect_tag = models.ForeignKey(Tag, related_name='%(class)s_tag', on_delete=models.CASCADE, null=True, blank=True,
                                    verbose_name='Tag подборки')
    panels = [
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
            FieldPanel('collect'),
            FieldPanel('collect_tag'),
        ], heading="Данные календаря"),
    ]

    class Meta:
        verbose_name = 'Изображение слайдера'
        verbose_name_plural = 'Изображения слайдера'
