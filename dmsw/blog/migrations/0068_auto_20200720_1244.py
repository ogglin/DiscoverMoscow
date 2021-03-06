# Generated by Django 3.0.5 on 2020-07-20 09:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0067_auto_20200714_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='show_image_on_mobile',
            field=models.BooleanField(blank=True, default=False, verbose_name='показывать "Изображение заголовка на фон" на мобильных'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 20, 8, 44, 15, 195713, tzinfo=utc), verbose_name='Время публикации'),
        ),
    ]
