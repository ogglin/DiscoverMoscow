# Generated by Django 3.0.5 on 2020-04-27 15:47

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('blog', '0036_blogpage_main_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='main_color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='blog.ColoredTag', verbose_name='Основной цвет'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='blog.BlogPageTag', to='taggit.Tag', verbose_name='Дополнительные теги'),
        ),
    ]
