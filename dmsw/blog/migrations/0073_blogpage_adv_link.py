# Generated by Django 3.0.5 on 2020-05-05 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0072_auto_20200504_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='adv_link',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на рекламодателя'),
        ),
    ]