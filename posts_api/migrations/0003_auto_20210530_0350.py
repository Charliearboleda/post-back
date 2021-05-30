# Generated by Django 3.2.3 on 2021-05-30 03:50

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_api', '0002_auto_20210530_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=0), size=None),
        ),
        migrations.AlterField(
            model_name='post',
            name='liked_by',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=0), size=None),
        ),
    ]
