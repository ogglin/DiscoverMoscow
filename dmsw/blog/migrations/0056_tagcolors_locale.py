# Generated by Django 3.0.5 on 2020-05-26 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0055_auto_20200520_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagcolors',
            name='locale',
            field=models.CharField(choices=[('ru', 'ru'), ('en', 'en')], default='ru', max_length=250, verbose_name='Language'),
        ),
    ]