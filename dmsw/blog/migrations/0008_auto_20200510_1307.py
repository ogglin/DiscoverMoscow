# Generated by Django 3.0.5 on 2020-05-10 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_mediakit'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mediakit',
            options={'verbose_name_plural': 'Медиакит'},
        ),
        migrations.RemoveField(
            model_name='mediakit',
            name='media_kit',
        ),
    ]
