# Generated by Django 3.0.5 on 2020-05-13 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_blogpage_main_color_sel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='main_color_sel',
        ),
    ]
