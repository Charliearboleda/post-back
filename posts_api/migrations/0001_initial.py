# Generated by Django 3.2.3 on 2021-05-25 23:35

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.IntegerField()),
                ('image', models.CharField(max_length=128)),
                ('text', models.CharField(max_length=140)),
                ('liked_by', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('comments', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
            ],
        ),
    ]
