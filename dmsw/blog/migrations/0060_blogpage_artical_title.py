# Generated by Django 3.0.5 on 2020-05-02 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0059_auto_20200502_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='artical_title',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Заголовок для статьи'),
        ),
    ]
