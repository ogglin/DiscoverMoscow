# Generated by Django 3.0.5 on 2020-05-04 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0068_searchpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='coloredtag',
            name='order_num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
