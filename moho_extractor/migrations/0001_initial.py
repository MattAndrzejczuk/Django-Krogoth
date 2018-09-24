# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-24 05:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('krogoth_gantry', '0002_auto_20180924_0517'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='NgIncludedHtml',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('contents', models.TextField(default='<h4> krogoth_gantry Error: There is nothing here yet! </h4>')),
                ('url_helper', models.CharField(default='Dont worry about this text.', help_text='krogoth_gantry will take care of this.', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NgIncludedJs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('contents', models.TextField(default='/*NgIncludedJs*/')),
                ('url_helper', models.CharField(default='Dont worry about this text.', help_text='krogoth_gantry will take care of this.', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IncludedHtmlCoreTemplate',
            fields=[
                ('ngincludedhtml_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='moho_extractor.NgIncludedHtml')),
                ('file_name', models.CharField(default='/usr/src/app/', max_length=256)),
                ('os_path', models.CharField(default='/usr/src/app/', max_length=256)),
                ('meta_kind_0', models.CharField(default='Layout', max_length=160)),
                ('meta_kind_1', models.CharField(default='Horizontal', max_length=160)),
                ('meta_kind_2', models.CharField(default='n/a', max_length=160)),
            ],
            options={
                'abstract': False,
            },
            bases=('moho_extractor.ngincludedhtml',),
        ),
        migrations.CreateModel(
            name='IncludedHtmlMaster',
            fields=[
                ('ngincludedhtml_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='moho_extractor.NgIncludedHtml')),
                ('sys_path', models.CharField(default='/usr/src/app/', max_length=256)),
                ('master_vc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partial_html', to='krogoth_gantry.KrogothGantryMasterViewController')),
            ],
            options={
                'abstract': False,
            },
            bases=('moho_extractor.ngincludedhtml',),
        ),
        migrations.CreateModel(
            name='IncludedJsMaster',
            fields=[
                ('ngincludedjs_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='moho_extractor.NgIncludedJs')),
                ('sys_path', models.CharField(default='/usr/src/app/', max_length=256)),
                ('master_vc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partial_js', to='krogoth_gantry.KrogothGantryMasterViewController')),
            ],
            options={
                'abstract': False,
            },
            bases=('moho_extractor.ngincludedjs',),
        ),
        migrations.AddField(
            model_name='ngincludedjs',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_moho_extractor.ngincludedjs_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='ngincludedhtml',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_moho_extractor.ngincludedhtml_set+', to='contenttypes.ContentType'),
        ),
    ]
