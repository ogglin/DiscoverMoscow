import os
from colorfield.fields import ColorField
from django.db import models
from django import forms
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from blog.models import Tags


# Create your models here.

class Sliders(models.Model):
    slider_types = [
        ('standart', 'Стандарт'),
        ('calendar', 'Календарь'),
    ]
    locales = [
        ('ru', 'ru'),
        ('en', 'en'),
    ]
    locale = models.CharField(max_length=250, verbose_name="Language", choices=locales, default='ru')
    order_num = models.IntegerField('Порядок', null=False, blank=True, default=999)
    ontop = models.BooleanField('в начало', null=True, blank=True, default=False)
    draft = models.BooleanField('черновик', null=True, blank=True, default=False)
    color = ColorField(default='#FFFFFF', verbose_name="цвет")
    title = models.CharField(max_length=128, null=True, blank=True, verbose_name="заголовок")
    subtitle = models.CharField(blank=True, max_length=250, verbose_name="подзаголовок")
    standart_link = models.CharField(blank=True, max_length=255, verbose_name="ссылка")
    image = models.ForeignKey('wagtailimages.Image', blank=True, null=True, on_delete=models.CASCADE, related_name='+',
                              verbose_name="Основное изображение",
                              )
    calendar_image = models.ForeignKey('wagtailimages.Image', blank=True, null=True, on_delete=models.CASCADE,
                                       related_name='+', verbose_name="Изображение в календарь",
                                       )
    slider_type = models.CharField(max_length=250, choices=slider_types, default='black', verbose_name="Тип слайда")
    title_one = models.CharField(max_length=250, blank=True, verbose_name="подзаголовок 1")
    tag_link_one = models.CharField(blank=True, max_length=255, verbose_name="ссылка 1")
    title_two = models.CharField(max_length=250, blank=True, verbose_name="подзаголовок 2")
    tag_link_two = models.CharField(blank=True, max_length=255, verbose_name="ссылка 2")
    title_three = models.CharField(max_length=250, blank=True, verbose_name="подзаголовок 3")
    tag_link_three = models.CharField(blank=True, max_length=255, verbose_name="ссылка 3")
    collect = models.CharField(blank=True, max_length=255, verbose_name="название подборки")
    collect_tag = models.ForeignKey(Tags, related_name='%(class)s_tag', on_delete=models.CASCADE, null=True, blank=True,
                                    verbose_name='Tag подборки')
    panels = [
        MultiFieldPanel([
            FieldPanel('order_num'),
            FieldPanel('ontop', widget=forms.CheckboxInput),
            FieldPanel('draft', widget=forms.CheckboxInput),
            FieldPanel('slider_type'),
            FieldPanel('title'),
            FieldPanel('subtitle'),
            FieldPanel('color'),
            FieldPanel('standart_link'),
        ], heading="Данные слайдера"),
        ImageChooserPanel('image'),
        MultiFieldPanel([
            ImageChooserPanel('calendar_image'),
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
        ordering = ['-ontop', 'order_num', 'draft', '-id']


class SlidersEN(Sliders):
    locale = 'en'

    def save(self, *args, **kwargs):
        self.locale = 'en'
        return super().save(*args, **kwargs)
