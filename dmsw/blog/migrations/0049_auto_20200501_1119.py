# Generated by Django 3.0.5 on 2020-05-01 08:19

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0048_auto_20200501_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='content_body',
            field=wagtail.core.fields.StreamField([('container', wagtail.core.blocks.StructBlock([('onecol', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock())], blank=True, icon='cog', label='Одна колонка', null=True, required=False)), ('twocol', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock())], blank=True, icon='arrow-right', label='Left column content', null=True, required=False)), ('right_column', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock())], blank=True, icon='arrow-right', label='Right column content', null=True, required=False))], blank=True, icon='cog', label='Две колонки', null=True, required=False))])), ('container_narrow', wagtail.core.blocks.StructBlock([('onecol', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock())], blank=True, icon='cog', label='Одна колонка', null=True, required=False)), ('twocol', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock())], blank=True, icon='arrow-right', label='Left column content', null=True, required=False)), ('right_column', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock())], blank=True, icon='arrow-right', label='Right column content', null=True, required=False))], blank=True, icon='cog', label='Две колонки', null=True, required=False))])), ('container_wide', wagtail.core.blocks.StructBlock([('onecol', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock())], blank=True, icon='cog', label='Одна колонка', null=True, required=False)), ('twocol', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock())], blank=True, icon='arrow-right', label='Left column content', null=True, required=False)), ('right_column', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock())], blank=True, icon='arrow-right', label='Right column content', null=True, required=False))], blank=True, icon='cog', label='Две колонки', null=True, required=False))]))], blank=True, null=True, verbose_name='Статья'),
        ),
    ]