from django.db import models
from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


# class ImageItem(blocks.StreamBlock):
#     embed = ImageChooserBlock(verbose_name='Изображение')
#     title = blocks.RichTextBlock(verbose_name='Подпись')
#     link = models.CharField(max_length=255, blank=True, null=True, verbose_name='Ссылка')
#     meta = models.CharField(max_length=255, blank=True, null=True, verbose_name='Мета информация')
#
#     class Meta:
#         template = 'blog/blocks/image_item.html'


class GalleryBlock(blocks.StreamBlock):
    image = ImageChooserBlock()

    class Meta:
        template = 'blog/blocks/gallery_block.html'


class PartnerBlock(blocks.StreamBlock):
    image = ImageChooserBlock()
    paragraph = blocks.RichTextBlock()

    class Meta:
        template = 'blog/blocks/partner_block.html'


class VideoBlock(blocks.StreamBlock):
    video = EmbedBlock()
    paragraph = blocks.RichTextBlock()

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
    video = blocks.RichTextBlock(label='Добавить видео')

    class Meta:
        template = 'blog/blocks/video_gallery.html'


class СharitableItem(blocks.StreamBlock):
    main_image = ImageChooserBlock()
    body_text = blocks.RichTextBlock()
    help_link = blocks.CharBlock(verbose_name='Ссылка на кнопку Помочь')
    contact_link = blocks.CharBlock(verbose_name='Ссылка на кнопку Контакт')

    class Meta:
        template = 'blog/blocks/charitable_block.html'


class ImageLinkedBlock(blocks.StreamBlock):
    image = ImageChooserBlock(label='Изображение')
    link = blocks.TextBlock(icon='link', label='Ссылка')
    title = blocks.RichTextBlock(verbose_name='Подпись')
    meta = blocks.RichTextBlock(verbose_name='Мета информация')

    class Meta:
        template = 'blog/blocks/image_linked_block.html'


class ColumnBlock(blocks.StreamBlock):
    paragraph = blocks.RichTextBlock()
    image = ImageChooserBlock(label='Изображение')
    linked_image = ImageLinkedBlock(label='Изображение с сылкой', icon='image')
    video = VideoBlock(icon='placeholder', label='Видео блок', null=True, blank=True, required=False)
    yt_video = VideoGallery(icon='placeholder', label='Видео галерея', null=True, blank=True, required=False)
    html = blocks.RawHTMLBlock()
    gallery = GalleryBlock(icon='image', label='Галерея изображений', null=True, blank=True, required=False)
    partner = PartnerBlock(icon='placeholder', label='Блок партнера', null=True, blank=True, required=False)
    charitable = СharitableItem(icon='placeholder', label='Блок благотворительность', null=True, blank=True,
                                required=False)

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
