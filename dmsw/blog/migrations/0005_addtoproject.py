# Generated by Django 3.0.5 on 2020-05-10 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_coloredtag_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddToProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тема письма')),
            ],
        ),
    ]