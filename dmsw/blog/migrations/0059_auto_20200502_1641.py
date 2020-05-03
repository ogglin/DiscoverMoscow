# Generated by Django 3.0.5 on 2020-05-02 13:41

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('blog', '0058_auto_20200502_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='artical_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Изображение для статьи'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='content_body',
            field=wagtail.core.fields.StreamField([('container', wagtail.core.blocks.StructBlock([('onecol', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видер блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StreamBlock([('add_video', wagtail.core.blocks.RawHTMLBlock())], blank=True, icon='placeholder', label='Видер по id', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея', null=True, required=False))], blank=True, icon='cog', label='Одна колонка', null=True, required=False)), ('twocol', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видер блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StreamBlock([('add_video', wagtail.core.blocks.RawHTMLBlock())], blank=True, icon='placeholder', label='Видер по id', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея', null=True, required=False))], blank=True, icon='arrow-right', label='Left column content', null=True, required=False)), ('right_column', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видер блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StreamBlock([('add_video', wagtail.core.blocks.RawHTMLBlock())], blank=True, icon='placeholder', label='Видер по id', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея', null=True, required=False))], blank=True, icon='arrow-right', label='Right column content', null=True, required=False))], blank=True, icon='cog', label='Две колонки', null=True, required=False))])), ('container_narrow', wagtail.core.blocks.StructBlock([('onecol', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видер блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StreamBlock([('add_video', wagtail.core.blocks.RawHTMLBlock())], blank=True, icon='placeholder', label='Видер по id', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея', null=True, required=False))], blank=True, icon='cog', label='Одна колонка', null=True, required=False)), ('twocol', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видер блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StreamBlock([('add_video', wagtail.core.blocks.RawHTMLBlock())], blank=True, icon='placeholder', label='Видер по id', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея', null=True, required=False))], blank=True, icon='arrow-right', label='Left column content', null=True, required=False)), ('right_column', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видер блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StreamBlock([('add_video', wagtail.core.blocks.RawHTMLBlock())], blank=True, icon='placeholder', label='Видер по id', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея', null=True, required=False))], blank=True, icon='arrow-right', label='Right column content', null=True, required=False))], blank=True, icon='cog', label='Две колонки', null=True, required=False))])), ('container_wide', wagtail.core.blocks.StructBlock([('onecol', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видер блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StreamBlock([('add_video', wagtail.core.blocks.RawHTMLBlock())], blank=True, icon='placeholder', label='Видер по id', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея', null=True, required=False))], blank=True, icon='cog', label='Одна колонка', null=True, required=False)), ('twocol', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видер блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StreamBlock([('add_video', wagtail.core.blocks.RawHTMLBlock())], blank=True, icon='placeholder', label='Видер по id', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея', null=True, required=False))], blank=True, icon='arrow-right', label='Left column content', null=True, required=False)), ('right_column', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видер блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StreamBlock([('add_video', wagtail.core.blocks.RawHTMLBlock())], blank=True, icon='placeholder', label='Видер по id', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея', null=True, required=False))], blank=True, icon='arrow-right', label='Right column content', null=True, required=False))], blank=True, icon='cog', label='Две колонки', null=True, required=False))]))], blank=True, null=True, verbose_name='Статья'),
        ),
    ]
