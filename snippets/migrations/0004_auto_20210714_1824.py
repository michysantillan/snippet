# Generated by Django 2.2.4 on 2021-07-14 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_auto_20210714_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
