# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 23:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('organization_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='organizations.Organization')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('url', models.URLField(blank=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
                ('fax', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=('organizations.organization',),
        ),
    ]