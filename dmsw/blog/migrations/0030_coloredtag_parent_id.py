# Generated by Django 3.0.5 on 2020-04-27 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_auto_20200426_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='coloredtag',
            name='parent_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.ColoredTag'),
        ),
    ]
