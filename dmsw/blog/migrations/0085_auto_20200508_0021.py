# Generated by Django 3.0.5 on 2020-05-07 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0084_auto_20200508_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coloredtag',
            name='order',
            field=models.IntegerField(choices=[(0, 'Главное меню'), (1, 'под меню')], default=1, verbose_name='Уровень меню'),
        ),
    ]