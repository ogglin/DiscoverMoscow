# Generated by Django 3.0.5 on 2020-05-05 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0073_blogpage_adv_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='adv_link',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Ссылка на рекламодателя'),
        ),
    ]
