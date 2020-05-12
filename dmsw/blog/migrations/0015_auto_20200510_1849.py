# Generated by Django 3.0.5 on 2020-05-10 15:49

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20200510_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='content_body',
            field=wagtail.core.fields.StreamField([('container', wagtail.core.blocks.StructBlock([('onecol', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видео блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StructBlock([('element', wagtail.core.blocks.StreamBlock([], blank=True, icon='video', label='Добавить видео', null=True, required=False))], blank=True, icon='placeholder', label='Видео галерея', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея', null=True, required=False))], blank=True, icon='cog', label='Одна колонка', null=True, required=False)), ('twocol', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видео блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StructBlock([('element', wagtail.core.blocks.StreamBlock([], blank=True, icon='video', label='Добавить видео', null=True, required=False))], blank=True, icon='placeholder', label='Видео галерея', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея', null=True, required=False))], blank=True, icon='arrow-right', label='Left column content', null=True, required=False)), ('right_column', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видео блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StructBlock([('element', wagtail.core.blocks.StreamBlock([], blank=True, icon='video', label='Добавить видео', null=True, required=False))], blank=True, icon='placeholder', label='Видео галерея', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея', null=True, required=False))], blank=True, icon='arrow-right', label='Right column content', null=True, required=False))], blank=True, icon='cog', label='Две колонки', null=True, required=False))])), ('container_narrow', wagtail.core.blocks.StructBlock([('onecol', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видео блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StructBlock([('element', wagtail.core.blocks.StreamBlock([], blank=True, icon='video', label='Добавить видео', null=True, required=False))], blank=True, icon='placeholder', label='Видео галерея', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея', null=True, required=False))], blank=True, icon='cog', label='Одна колонка', null=True, required=False)), ('twocol', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видео блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StructBlock([('element', wagtail.core.blocks.StreamBlock([], blank=True, icon='video', label='Добавить видео', null=True, required=False))], blank=True, icon='placeholder', label='Видео галерея', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея', null=True, required=False))], blank=True, icon='arrow-right', label='Left column content', null=True, required=False)), ('right_column', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видео блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StructBlock([('element', wagtail.core.blocks.StreamBlock([], blank=True, icon='video', label='Добавить видео', null=True, required=False))], blank=True, icon='placeholder', label='Видео галерея', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея', null=True, required=False))], blank=True, icon='arrow-right', label='Right column content', null=True, required=False))], blank=True, icon='cog', label='Две колонки', null=True, required=False))])), ('container_wide', wagtail.core.blocks.StructBlock([('onecol', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видео блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StructBlock([('element', wagtail.core.blocks.StreamBlock([], blank=True, icon='video', label='Добавить видео', null=True, required=False))], blank=True, icon='placeholder', label='Видео галерея', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея', null=True, required=False))], blank=True, icon='cog', label='Одна колонка', null=True, required=False)), ('twocol', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видео блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StructBlock([('element', wagtail.core.blocks.StreamBlock([], blank=True, icon='video', label='Добавить видео', null=True, required=False))], blank=True, icon='placeholder', label='Видео галерея', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея', null=True, required=False))], blank=True, icon='arrow-right', label='Left column content', null=True, required=False)), ('right_column', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видео блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StructBlock([('element', wagtail.core.blocks.StreamBlock([], blank=True, icon='video', label='Добавить видео', null=True, required=False))], blank=True, icon='placeholder', label='Видео галерея', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея', null=True, required=False))], blank=True, icon='arrow-right', label='Right column content', null=True, required=False))], blank=True, icon='cog', label='Две колонки', null=True, required=False))]))], blank=True, null=True, verbose_name='Статья'),
        ),
    ]