# Generated by Django 3.2.3 on 2021-05-31 03:55

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_api', '0002_auto_20210531_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='following',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='posts',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None),
        ),
    ]
