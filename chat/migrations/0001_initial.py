# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=400)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='JawnUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_pic', models.ImageField(null=True, upload_to=b'media/', blank=True)),
                ('about_me', models.CharField(max_length=400, null=True, blank=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('sex', models.CharField(blank=True, max_length=10, null=True, choices=[(b'male', b'Male'), (b'female', b'Female')])),
                ('base_user', models.OneToOneField(related_name='jawn_user', to=settings.AUTH_USER_MODEL)),
                ('follows', models.ManyToManyField(related_name='followed_by', null=True, to='chat.JawnUser', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageMessage',
            fields=[
                ('message_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='chat.Message')),
                ('type', models.CharField(default=b'image', max_length=50, choices=[(b'image', b'image')])),
                ('image_url', models.ImageField(upload_to=b'media/')),
                ('caption', models.TextField(max_length=1000, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('chat.message',),
        ),
        migrations.CreateModel(
            name='TextMessage',
            fields=[
                ('message_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='chat.Message')),
                ('type', models.CharField(default=b'text', max_length=50, choices=[(b'text', b'text')])),
                ('text', models.TextField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
            bases=('chat.message',),
        ),
        migrations.AddField(
            model_name='message',
            name='channel',
            field=models.ForeignKey(related_name='messages', to='chat.Channel'),
        ),
        migrations.AddField(
            model_name='message',
            name='jawn_user',
            field=models.ForeignKey(related_name='user', to='chat.JawnUser'),
        ),
        migrations.AddField(
            model_name='message',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_chat.message_set+', editable=False, to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='channel',
            name='creator',
            field=models.ForeignKey(related_name='creator', to='chat.JawnUser'),
        ),
    ]
