# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-08 19:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('status', models.BooleanField()),
                ('featured_photo', models.ImageField(upload_to=b'')),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Tag'),
        ),
    ]