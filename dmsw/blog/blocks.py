from django.db import models
from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class GalleryBlock(blocks.StreamBlock):
    image = ImageChooserBlock()

    class Meta:
        template = 'blog/blocks/gallery_block.html'


class VideoBlock(blocks.StreamBlock):
    video = EmbedBlock()

    class Meta:
        template = 'blog/blocks/video_block.html'


class VideoItem(blocks.StreamBlock):
    embed = models.CharField(max_length=255, blank=True, null=True, verbose_name='Ссылка на видео')
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Заголовок')
    sub_title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Подзаголовок')
    meta = models.CharField(max_length=255, blank=True, null=True, verbose_name='Мета информация')

    class Meta:
        template = 'blog/blocks/video_item.html'

class VideoGallery(blocks.StreamBlock):
    video = blocks.RichTextBlock()
    element = VideoItem(icon='video', label='Добавить видео', null=True, blank=True, required=False)

    class Meta:
        template = 'blog/blocks/video_gallery.html'


class ColumnBlock(blocks.StreamBlock):
    paragraph = blocks.RichTextBlock()
    image = ImageChooserBlock()
    video = VideoBlock(icon='placeholder', label='Видео блок', null=True, blank=True, required=False)
    yt_video = VideoGallery(icon='placeholder', label='Видео галерея', null=True, blank=True, required=False)
    html = blocks.RawHTMLBlock()
    gallery = GalleryBlock(icon='image', label='Галерея', null=True, blank=True, required=False)

    class Meta:
        template = 'blog/blocks/column_block.html'
        form_classname = 'col6'


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