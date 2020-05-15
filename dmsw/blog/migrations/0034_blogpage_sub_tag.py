# Generated by Django 3.0.5 on 2020-05-14 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_remove_blogpage_sub_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='sub_tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='blog.Tag', verbose_name='Дополнительный тег'),
        ),
    ]
