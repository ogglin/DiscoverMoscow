# Generated by Django 3.0.5 on 2020-05-14 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20200514_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='sub_tag',
        ),
    ]
