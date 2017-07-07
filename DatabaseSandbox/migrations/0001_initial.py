# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-07 00:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicUploadTrackerSB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100)),
                ('download_url', models.CharField(max_length=255)),
                ('system_path', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LazarusCommanderAccountSB',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_suspended', models.BooleanField(default=False)),
                ('is_terminated', models.BooleanField(default=False)),
                ('faction', models.CharField(choices=[('Arm', 'Arm'), ('Core', 'Core')], max_length=25)),
                ('profile_pic', models.CharField(max_length=255)),
                ('about_me', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='LazarusModProjectSB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_created=True)),
                ('unique_name', models.CharField(max_length=100, unique=True)),
                ('date_modified', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='VisitorLogSB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_created=True)),
                ('remote_addr', models.CharField(blank=True, max_length=255, null=True)),
                ('http_usr', models.CharField(blank=True, max_length=255, null=True)),
                ('http_accept', models.CharField(blank=True, max_length=255, null=True)),
                ('other_misc_notes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
