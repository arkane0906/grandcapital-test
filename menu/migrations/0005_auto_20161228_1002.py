# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 10:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20161227_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('url', models.CharField(blank=True, max_length=250, null=True, verbose_name='Адрес ссылки')),
                ('level', models.PositiveSmallIntegerField(default=0, editable=False, verbose_name='Уровень')),
                ('position', models.PositiveSmallIntegerField(default=0, editable=False, verbose_name='Позиция')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.MenuItem', verbose_name='Родительский пункт меню')),
            ],
            options={
                'verbose_name': 'Menu item',
                'verbose_name_plural': 'Menu items',
            },
        ),
        migrations.RemoveField(
            model_name='item',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]