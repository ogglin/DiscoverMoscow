# Generated by Django 3.0.5 on 2020-05-07 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0078_auto_20200507_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coloredtag',
            name='parent_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Tag', verbose_name='Родительский тег'),
        ),
    ]