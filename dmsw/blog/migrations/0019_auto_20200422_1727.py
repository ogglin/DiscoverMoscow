# Generated by Django 3.0.5 on 2020-04-22 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20200422_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='animate_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Анимация'),
        ),
    ]
