# Generated by Django 3.0.5 on 2020-04-27 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0035_auto_20200427_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='main_tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='blog.Tag', verbose_name='Основной тег'),
        ),
    ]