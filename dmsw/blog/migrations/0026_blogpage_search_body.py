# Generated by Django 3.0.5 on 2020-05-13 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_formfield_formpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='search_body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
