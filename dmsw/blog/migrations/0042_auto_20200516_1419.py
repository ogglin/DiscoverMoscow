# Generated by Django 3.0.5 on 2020-05-16 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0041_auto_20200516_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='tag',
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='main_tag',
            field=models.ForeignKey(blank=True, limit_choices_to={'parent_id_id__isnull': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='blog.Tags', verbose_name='Основной тег'),
        ),
    ]
