from django.db import models
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class LocaleLink(blocks.StreamBlock):
    link = blocks.RichTextBlock()

    class Meta:
        template = 'guides/blocks/locale_link.html'


class GuideBlock(blocks.StreamBlock):
    title = blocks.CharBlock(verbose_name='Title')
    image = ImageChooserBlock()
    paragraph = blocks.RichTextBlock()
    file = blocks.RichTextBlock()

    class Meta:
        template = 'guides/blocks/guide_block.html'

