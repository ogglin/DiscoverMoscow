# Generated by Django 3.0.5 on 2020-06-01 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dop_slider', '0015_auto_20200526_1135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sliders',
            options={'ordering': ['-id'], 'verbose_name': 'Изображение слайдера', 'verbose_name_plural': 'Изображения слайдера'},
        ),
    ]
