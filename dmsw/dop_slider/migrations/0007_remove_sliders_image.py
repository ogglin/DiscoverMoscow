# Generated by Django 3.0.5 on 2020-05-02 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dop_slider', '0006_auto_20200502_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sliders',
            name='image',
        ),
    ]
