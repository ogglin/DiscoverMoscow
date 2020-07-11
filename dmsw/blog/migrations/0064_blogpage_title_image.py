# Generated by Django 3.0.5 on 2020-07-09 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('blog', '0063_auto_20200709_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='title_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Изображение заголовка на фон'),
        ),
    ]