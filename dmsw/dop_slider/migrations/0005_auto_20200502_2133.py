# Generated by Django 3.0.5 on 2020-05-02 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dop_slider', '0004_auto_20200502_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliders',
            name='standart_link',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
