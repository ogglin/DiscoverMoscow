# Generated by Django 3.0.5 on 2020-05-13 13:46

from django.db import migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20200513_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='main_color_sel',
            field=smart_selects.db_fields.ChainedManyToManyField(chained_field='tag_id', chained_model_field='tag_id', to='blog.TagColors'),
        ),
    ]
