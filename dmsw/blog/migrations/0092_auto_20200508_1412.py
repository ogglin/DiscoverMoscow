# Generated by Django 3.0.5 on 2020-05-08 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0091_auto_20200508_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='main_color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='blog.TagColors', verbose_name='Основной цвет'),
        ),
    ]
