# Generated by Django 3.0.5 on 2020-04-30 21:54

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0045_auto_20200501_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='content_body',
            field=wagtail.core.fields.StreamField([('container', wagtail.core.blocks.StructBlock([('onecol', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock())], icon='cog', label='Одна колонка')), ('twocol', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock())], icon='arrow-right', label='Left column content')), ('right_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock())], icon='arrow-right', label='Right column content'))], icon='cog', label='Две колонки'))])), ('container_narrow', wagtail.core.blocks.StructBlock([('onecol', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock())], icon='cog', label='Одна колонка')), ('twocol', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock())], icon='arrow-right', label='Left column content')), ('right_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock())], icon='arrow-right', label='Right column content'))], icon='cog', label='Две колонки'))])), ('container_wide', wagtail.core.blocks.StructBlock([('onecol', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock())], icon='cog', label='Одна колонка')), ('twocol', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock())], icon='arrow-right', label='Left column content')), ('right_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.embeds.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock())], icon='arrow-right', label='Right column content'))], icon='cog', label='Две колонки'))]))], blank=True, null=True, verbose_name='Статья'),
        ),
    ]
