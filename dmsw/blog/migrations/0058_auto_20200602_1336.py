# Generated by Django 3.0.5 on 2020-06-02 10:36

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0057_auto_20200601_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypedPageEN',
            fields=[
                ('typedpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.TypedPage')),
            ],
            options={
                'verbose_name': "Typed page in english (don't use or modify)",
            },
            bases=('blog.typedpage',),
        ),
        migrations.AddField(
            model_name='typedpage',
            name='locale',
            field=models.CharField(choices=[('ru', 'ru'), ('en', 'en')], default='ru', max_length=250, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='content_body',
            field=wagtail.core.fields.StreamField([('container', wagtail.core.blocks.StructBlock([('onecol', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(label='Изображение')), ('linked_image', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Изображение')), ('link', wagtail.core.blocks.TextBlock(icon='link', label='Ссылка'))], icon='image', label='Изображение с сылкой')), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видео блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StreamBlock([('video', wagtail.core.blocks.RichTextBlock(label='Добавить видео'))], blank=True, icon='placeholder', label='Видео галерея', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея изображений', null=True, required=False)), ('partner', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock())], blank=True, icon='placeholder', label='Блок партнера', null=True, required=False)), ('charitable', wagtail.core.blocks.StreamBlock([('main_image', wagtail.images.blocks.ImageChooserBlock()), ('body_text', wagtail.core.blocks.RichTextBlock()), ('help_link', wagtail.core.blocks.CharBlock(verbose_name='Ссылка на кнопку Помочь')), ('contact_link', wagtail.core.blocks.CharBlock(verbose_name='Ссылка на кнопку Контакт'))], blank=True, icon='placeholder', label='Блок благотворительность', null=True, required=False))], blank=True, icon='cog', label='Одна колонка', null=True, required=False)), ('twocol', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(label='Изображение')), ('linked_image', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Изображение')), ('link', wagtail.core.blocks.TextBlock(icon='link', label='Ссылка'))], icon='image', label='Изображение с сылкой')), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видео блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StreamBlock([('video', wagtail.core.blocks.RichTextBlock(label='Добавить видео'))], blank=True, icon='placeholder', label='Видео галерея', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея изображений', null=True, required=False)), ('partner', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock())], blank=True, icon='placeholder', label='Блок партнера', null=True, required=False)), ('charitable', wagtail.core.blocks.StreamBlock([('main_image', wagtail.images.blocks.ImageChooserBlock()), ('body_text', wagtail.core.blocks.RichTextBlock()), ('help_link', wagtail.core.blocks.CharBlock(verbose_name='Ссылка на кнопку Помочь')), ('contact_link', wagtail.core.blocks.CharBlock(verbose_name='Ссылка на кнопку Контакт'))], blank=True, icon='placeholder', label='Блок благотворительность', null=True, required=False))], blank=True, icon='arrow-right', label='Left column content', null=True, required=False)), ('right_column', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(label='Изображение')), ('linked_image', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Изображение')), ('link', wagtail.core.blocks.TextBlock(icon='link', label='Ссылка'))], icon='image', label='Изображение с сылкой')), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видео блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StreamBlock([('video', wagtail.core.blocks.RichTextBlock(label='Добавить видео'))], blank=True, icon='placeholder', label='Видео галерея', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея изображений', null=True, required=False)), ('partner', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock())], blank=True, icon='placeholder', label='Блок партнера', null=True, required=False)), ('charitable', wagtail.core.blocks.StreamBlock([('main_image', wagtail.images.blocks.ImageChooserBlock()), ('body_text', wagtail.core.blocks.RichTextBlock()), ('help_link', wagtail.core.blocks.CharBlock(verbose_name='Ссылка на кнопку Помочь')), ('contact_link', wagtail.core.blocks.CharBlock(verbose_name='Ссылка на кнопку Контакт'))], blank=True, icon='placeholder', label='Блок благотворительность', null=True, required=False))], blank=True, icon='arrow-right', label='Right column content', null=True, required=False))], blank=True, icon='cog', label='Две колонки', null=True, required=False))])), ('container_narrow', wagtail.core.blocks.StructBlock([('onecol', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(label='Изображение')), ('linked_image', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Изображение')), ('link', wagtail.core.blocks.TextBlock(icon='link', label='Ссылка'))], icon='image', label='Изображение с сылкой')), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видео блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StreamBlock([('video', wagtail.core.blocks.RichTextBlock(label='Добавить видео'))], blank=True, icon='placeholder', label='Видео галерея', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея изображений', null=True, required=False)), ('partner', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock())], blank=True, icon='placeholder', label='Блок партнера', null=True, required=False)), ('charitable', wagtail.core.blocks.StreamBlock([('main_image', wagtail.images.blocks.ImageChooserBlock()), ('body_text', wagtail.core.blocks.RichTextBlock()), ('help_link', wagtail.core.blocks.CharBlock(verbose_name='Ссылка на кнопку Помочь')), ('contact_link', wagtail.core.blocks.CharBlock(verbose_name='Ссылка на кнопку Контакт'))], blank=True, icon='placeholder', label='Блок благотворительность', null=True, required=False))], blank=True, icon='cog', label='Одна колонка', null=True, required=False)), ('twocol', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(label='Изображение')), ('linked_image', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Изображение')), ('link', wagtail.core.blocks.TextBlock(icon='link', label='Ссылка'))], icon='image', label='Изображение с сылкой')), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видео блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StreamBlock([('video', wagtail.core.blocks.RichTextBlock(label='Добавить видео'))], blank=True, icon='placeholder', label='Видео галерея', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея изображений', null=True, required=False)), ('partner', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock())], blank=True, icon='placeholder', label='Блок партнера', null=True, required=False)), ('charitable', wagtail.core.blocks.StreamBlock([('main_image', wagtail.images.blocks.ImageChooserBlock()), ('body_text', wagtail.core.blocks.RichTextBlock()), ('help_link', wagtail.core.blocks.CharBlock(verbose_name='Ссылка на кнопку Помочь')), ('contact_link', wagtail.core.blocks.CharBlock(verbose_name='Ссылка на кнопку Контакт'))], blank=True, icon='placeholder', label='Блок благотворительность', null=True, required=False))], blank=True, icon='arrow-right', label='Left column content', null=True, required=False)), ('right_column', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(label='Изображение')), ('linked_image', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Изображение')), ('link', wagtail.core.blocks.TextBlock(icon='link', label='Ссылка'))], icon='image', label='Изображение с сылкой')), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видео блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StreamBlock([('video', wagtail.core.blocks.RichTextBlock(label='Добавить видео'))], blank=True, icon='placeholder', label='Видео галерея', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея изображений', null=True, required=False)), ('partner', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock())], blank=True, icon='placeholder', label='Блок партнера', null=True, required=False)), ('charitable', wagtail.core.blocks.StreamBlock([('main_image', wagtail.images.blocks.ImageChooserBlock()), ('body_text', wagtail.core.blocks.RichTextBlock()), ('help_link', wagtail.core.blocks.CharBlock(verbose_name='Ссылка на кнопку Помочь')), ('contact_link', wagtail.core.blocks.CharBlock(verbose_name='Ссылка на кнопку Контакт'))], blank=True, icon='placeholder', label='Блок благотворительность', null=True, required=False))], blank=True, icon='arrow-right', label='Right column content', null=True, required=False))], blank=True, icon='cog', label='Две колонки', null=True, required=False))])), ('container_wide', wagtail.core.blocks.StructBlock([('onecol', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(label='Изображение')), ('linked_image', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Изображение')), ('link', wagtail.core.blocks.TextBlock(icon='link', label='Ссылка'))], icon='image', label='Изображение с сылкой')), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видео блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StreamBlock([('video', wagtail.core.blocks.RichTextBlock(label='Добавить видео'))], blank=True, icon='placeholder', label='Видео галерея', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея изображений', null=True, required=False)), ('partner', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock())], blank=True, icon='placeholder', label='Блок партнера', null=True, required=False)), ('charitable', wagtail.core.blocks.StreamBlock([('main_image', wagtail.images.blocks.ImageChooserBlock()), ('body_text', wagtail.core.blocks.RichTextBlock()), ('help_link', wagtail.core.blocks.CharBlock(verbose_name='Ссылка на кнопку Помочь')), ('contact_link', wagtail.core.blocks.CharBlock(verbose_name='Ссылка на кнопку Контакт'))], blank=True, icon='placeholder', label='Блок благотворительность', null=True, required=False))], blank=True, icon='cog', label='Одна колонка', null=True, required=False)), ('twocol', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(label='Изображение')), ('linked_image', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Изображение')), ('link', wagtail.core.blocks.TextBlock(icon='link', label='Ссылка'))], icon='image', label='Изображение с сылкой')), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видео блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StreamBlock([('video', wagtail.core.blocks.RichTextBlock(label='Добавить видео'))], blank=True, icon='placeholder', label='Видео галерея', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея изображений', null=True, required=False)), ('partner', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock())], blank=True, icon='placeholder', label='Блок партнера', null=True, required=False)), ('charitable', wagtail.core.blocks.StreamBlock([('main_image', wagtail.images.blocks.ImageChooserBlock()), ('body_text', wagtail.core.blocks.RichTextBlock()), ('help_link', wagtail.core.blocks.CharBlock(verbose_name='Ссылка на кнопку Помочь')), ('contact_link', wagtail.core.blocks.CharBlock(verbose_name='Ссылка на кнопку Контакт'))], blank=True, icon='placeholder', label='Блок благотворительность', null=True, required=False))], blank=True, icon='arrow-right', label='Left column content', null=True, required=False)), ('right_column', wagtail.core.blocks.StreamBlock([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(label='Изображение')), ('linked_image', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Изображение')), ('link', wagtail.core.blocks.TextBlock(icon='link', label='Ссылка'))], icon='image', label='Изображение с сылкой')), ('video', wagtail.core.blocks.StreamBlock([('video', wagtail.embeds.blocks.EmbedBlock())], blank=True, icon='placeholder', label='Видео блок', null=True, required=False)), ('yt_video', wagtail.core.blocks.StreamBlock([('video', wagtail.core.blocks.RichTextBlock(label='Добавить видео'))], blank=True, icon='placeholder', label='Видео галерея', null=True, required=False)), ('html', wagtail.core.blocks.RawHTMLBlock()), ('gallery', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, icon='image', label='Галерея изображений', null=True, required=False)), ('partner', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock())], blank=True, icon='placeholder', label='Блок партнера', null=True, required=False)), ('charitable', wagtail.core.blocks.StreamBlock([('main_image', wagtail.images.blocks.ImageChooserBlock()), ('body_text', wagtail.core.blocks.RichTextBlock()), ('help_link', wagtail.core.blocks.CharBlock(verbose_name='Ссылка на кнопку Помочь')), ('contact_link', wagtail.core.blocks.CharBlock(verbose_name='Ссылка на кнопку Контакт'))], blank=True, icon='placeholder', label='Блок благотворительность', null=True, required=False))], blank=True, icon='arrow-right', label='Right column content', null=True, required=False))], blank=True, icon='cog', label='Две колонки', null=True, required=False))]))], blank=True, null=True, verbose_name='Статья'),
        ),
    ]