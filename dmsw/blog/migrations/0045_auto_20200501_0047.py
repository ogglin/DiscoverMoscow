# Generated by Django 3.0.5 on 2020-04-30 21:47

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0044_auto_20200501_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='content_body',
            field=wagtail.core.fields.StreamField([('container', wagtail.core.blocks.StructBlock([])), ('container_narrow', wagtail.core.blocks.StructBlock([])), ('container_wide', wagtail.core.blocks.StructBlock([]))], blank=True, null=True, verbose_name='Статья'),
        ),
    ]