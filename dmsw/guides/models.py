from colorfield.fields import ColorField
from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, StreamFieldPanel, InlinePanel
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField

# Create your models here.
from wagtail.images.edit_handlers import ImageChooserPanel
from .blocks import *


class GuideMainPage(Page):
    main_title = models.CharField(max_length=256, verbose_name="Title", blank=False, null=False)
    color_one = ColorField(default='#FFFFFF', verbose_name='Color from')
    color_two = ColorField(default='#FFFFFF', verbose_name='Color to')

    guide_color = ColorField(default='#FFFFFF', verbose_name='Color for guides')
    guide_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Image for guides"
    )
    guide_content = StreamField([
        ('link', LocaleLink()),
    ], null=True, blank=True, verbose_name="Guides")

    map_color = ColorField(default='#FFFFFF', verbose_name='Color for maps')
    map_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Image for maps"
    )
    map_content = StreamField([
        ('link', LocaleLink()),
    ], null=True, blank=True, verbose_name='Maps')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('main_title'),
            FieldPanel('color_one'),
            FieldPanel('color_two')
        ], heading='Page header'),
        MultiFieldPanel([
            FieldPanel('guide_color'),
            ImageChooserPanel('guide_image'),
            StreamFieldPanel('guide_content'),
        ], heading='Guides block'),
        MultiFieldPanel([
            FieldPanel('map_color'),
            ImageChooserPanel('map_image'),
            StreamFieldPanel('map_content'),
        ], heading='Maps block')
    ]

    def get_template(self, request):
        return 'guides/guides_page.html'

    class Meta:
        verbose_name = "Guide main page"


class GuidePage(Page):
    main_title = models.CharField(max_length=256, verbose_name="Title", blank=False, null=False)
    color_one = ColorField(default='#FFFFFF', verbose_name='Color from')
    color_two = ColorField(default='#FFFFFF', verbose_name='Color to')
    background_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Background image"
    )
    main_content = StreamField([
        ('guide_block', GuideBlock()),
    ], null=True, blank=True, verbose_name='Maps')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('main_title'),
            FieldPanel('color_one'),
            FieldPanel('color_two'),
            ImageChooserPanel('background_image')
        ], heading='Page header'),
        MultiFieldPanel([
            StreamFieldPanel('main_content'),
        ], heading='Content block')
    ]

    def get_template(self, request):
        return 'guides/guide_page.html'

    class Meta:
        verbose_name = "Guide local page"
