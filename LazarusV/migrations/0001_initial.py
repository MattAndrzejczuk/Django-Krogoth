# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-29 20:11
from __future__ import unicode_literals

import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion
from django.contrib.postgres.operations import HStoreExtension

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('chat', '__first__'),
    ]

    operations = [
        HStoreExtension(),
        migrations.CreateModel(
            name='CavedogBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyname', models.CharField(max_length=250)),
                ('snowflake', models.CharField(max_length=50)),
                ('thumbnail_url', models.CharField(max_length=250)),
                ('raw_tdf', models.CharField(max_length=1550)),
                ('data_dict', django.contrib.postgres.fields.hstore.HStoreField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ModBuild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v_major', models.IntegerField(default=0)),
                ('v_minor', models.IntegerField(default=1)),
                ('download_url', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ModProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_public', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mod_developer', to='chat.JawnUser')),
            ],
        ),
        migrations.CreateModel(
            name='ModPublication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Untitled Mod Publication', max_length=50)),
                ('description', models.TextField(max_length=1000)),
                ('requirements', models.TextField(max_length=1000)),
                ('support', models.TextField(max_length=1000)),
                ('website_url', models.CharField(blank=True, max_length=150, null=True)),
                ('total_minor_milestones', models.IntegerField(blank=True, default=1, null=True)),
                ('total_major_milestones', models.IntegerField(blank=True, default=0, null=True)),
                ('kind', models.TextField(choices=[('alpha', 'Alpha'), ('beta', 'Beta'), ('rc', 'Release Candidate'), ('release', 'Release')], max_length=25)),
                ('is_private', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_votes', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WargameData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_name', models.CharField(max_length=50)),
                ('kind', models.CharField(max_length=50)),
                ('thumbnail_url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WargameFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=100)),
                ('unique_name', models.CharField(max_length=50)),
                ('kind', models.CharField(max_length=50)),
                ('thumbnail_url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WargamePackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('thumbnail_url', models.CharField(max_length=100)),
                ('parent_proj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LazarusV.ModProject')),
            ],
        ),
        migrations.CreateModel(
            name='LazarusBase',
            fields=[
                ('cavedogbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='LazarusV.CavedogBase')),
                ('is_deleted', models.BooleanField(default=False)),
                ('mod_proj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LazarusV.ModProject')),
            ],
            options={
                'abstract': False,
            },
            bases=('LazarusV.cavedogbase',),
        ),
        migrations.CreateModel(
            name='RatingCavedogBase',
            fields=[
                ('userrating_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='LazarusV.UserRating')),
                ('vote_value', models.IntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
            bases=('LazarusV.userrating',),
        ),
        migrations.CreateModel(
            name='RatingModPublication',
            fields=[
                ('userrating_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='LazarusV.UserRating')),
                ('vote_value', models.IntegerField(default=1)),
                ('lazarus_published_mod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lazarus_mod_distribution', to='LazarusV.ModPublication')),
            ],
            options={
                'abstract': False,
            },
            bases=('LazarusV.userrating',),
        ),
        migrations.AddField(
            model_name='wargamefile',
            name='pack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LazarusV.WargamePackage'),
        ),
        migrations.AddField(
            model_name='wargamedata',
            name='pack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LazarusV.WargamePackage'),
        ),
        migrations.AddField(
            model_name='userrating',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_lazarusv.userrating_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='userrating',
            name='rated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote_caster', to='chat.JawnUser'),
        ),
        migrations.AddField(
            model_name='modbuild',
            name='rated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='distribution', to='LazarusV.ModPublication'),
        ),
        migrations.AddField(
            model_name='cavedogbase',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_lazarusv.cavedogbase_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='wargamedata',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LazarusV.LazarusBase'),
        ),
        migrations.AddField(
            model_name='ratingcavedogbase',
            name='cavedog_base_tdf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cavedog_tdf', to='LazarusV.CavedogBase'),
        ),
    ]