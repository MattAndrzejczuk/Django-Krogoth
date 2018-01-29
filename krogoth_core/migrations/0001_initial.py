# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-29 02:41
from __future__ import unicode_literals

from django.contrib.postgres.operations import HStoreExtension
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        HStoreExtension(),
        migrations.CreateModel(
            name='AKBowerComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=250)),
                ('package_version', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=251)),
            ],
        ),
        migrations.CreateModel(
            name='AKCustomDependency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=250)),
                ('package_version', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=251)),
            ],
        ),
        migrations.CreateModel(
            name='AKFoundationAbstract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_name', models.CharField(max_length=90, unique=True)),
                ('first_name', models.CharField(help_text='EXAMPLES: index. index. toolbar. theming.', max_length=140)),
                ('last_name',
                 models.CharField(help_text='EXAMPLES: .controller .route .module .service', max_length=140)),
                ('code', models.TextField(default='Not Yet Generated.')),
                ('ext', models.CharField(help_text='EXAMPLES: html css js ', max_length=24)),
                ('path', models.CharField(default='/krogoth_core/AKThemes/Pro/',
                                          help_text='the path to the folder which contains this code.', max_length=90)),
                ('theme', models.CharField(default='/usr/src/app/krogoth_core/AKThemes/Pro/', max_length=90)),
                ('is_selected_theme', models.BooleanField(default=False)),
                ('custom_key_values', django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True)),
                ('polymorphic_ctype',
                 models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE,
                                   related_name='polymorphic_krogoth_core.akfoundationabstract_set+',
                                   to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AKFoundationAngularCore',
            fields=[
            ],
            options={
                'indexes': [],
                'verbose_name_plural': 'Core Application',
                'proxy': True,
                'verbose_name': 'Core Application',
            },
            bases=('krogoth_core.akfoundationabstract',),
        ),
        migrations.CreateModel(
            name='AKFoundationConfig',
            fields=[
            ],
            options={
                'indexes': [],
                'verbose_name_plural': 'Core Configuration',
                'proxy': True,
                'verbose_name': 'Core Configuration',
            },
            bases=('krogoth_core.akfoundationabstract',),
        ),
        migrations.CreateModel(
            name='AKFoundationDirectives',
            fields=[
            ],
            options={
                'indexes': [],
                'verbose_name_plural': 'Core Directives',
                'proxy': True,
                'verbose_name': 'Core Directive',
            },
            bases=('krogoth_core.akfoundationabstract',),
        ),
        migrations.CreateModel(
            name='AKFoundationFilters',
            fields=[
            ],
            options={
                'indexes': [],
                'verbose_name_plural': 'Core Filters',
                'proxy': True,
                'verbose_name': 'Core Filter',
            },
            bases=('krogoth_core.akfoundationabstract',),
        ),
        migrations.CreateModel(
            name='AKFoundationIndex',
            fields=[
            ],
            options={
                'indexes': [],
                'verbose_name_plural': 'AngularJS Index Foundation',
                'proxy': True,
                'verbose_name': 'AngularJS Index Foundation',
            },
            bases=('krogoth_core.akfoundationabstract',),
        ),
        migrations.CreateModel(
            name='AKFoundationMain',
            fields=[
            ],
            options={
                'indexes': [],
                'verbose_name_plural': 'AngularJS Main Foundation',
                'proxy': True,
                'verbose_name': 'AngularJS Main Foundation',
            },
            bases=('krogoth_core.akfoundationabstract',),
        ),
        migrations.CreateModel(
            name='AKFoundationNavigation',
            fields=[
            ],
            options={
                'indexes': [],
                'verbose_name_plural': 'Layout Navigation',
                'proxy': True,
                'verbose_name': 'Layout Navigation',
            },
            bases=('krogoth_core.akfoundationabstract',),
        ),
        migrations.CreateModel(
            name='AKFoundationQuickPanel',
            fields=[
            ],
            options={
                'indexes': [],
                'verbose_name_plural': 'Layout Quick Panel',
                'proxy': True,
                'verbose_name': 'Layout Quick Panel',
            },
            bases=('krogoth_core.akfoundationabstract',),
        ),
        migrations.CreateModel(
            name='AKFoundationRESTful',
            fields=[
            ],
            options={
                'indexes': [],
                'verbose_name_plural': 'AngularJS RESTful Foundation',
                'proxy': True,
                'verbose_name': 'AngularJS RESTful Foundation',
            },
            bases=('krogoth_core.akfoundationabstract',),
        ),
        migrations.CreateModel(
            name='AKFoundationThemingConfiguration',
            fields=[
            ],
            options={
                'indexes': [],
                'verbose_name_plural': 'Core Theming Options',
                'proxy': True,
                'verbose_name': 'Core Theming Option',
            },
            bases=('krogoth_core.akfoundationabstract',),
        ),
        migrations.CreateModel(
            name='AKFoundationThemingConstant',
            fields=[
            ],
            options={
                'indexes': [],
                'verbose_name_plural': 'Core Theming Constants',
                'proxy': True,
                'verbose_name': 'Core Theming Constant',
            },
            bases=('krogoth_core.akfoundationabstract',),
        ),
        migrations.CreateModel(
            name='AKFoundationThemingService',
            fields=[
            ],
            options={
                'indexes': [],
                'verbose_name_plural': 'Core Theming Services',
                'proxy': True,
                'verbose_name': 'Core Theming Service',
            },
            bases=('krogoth_core.akfoundationabstract',),
        ),
        migrations.CreateModel(
            name='AKFoundationToolbar',
            fields=[
            ],
            options={
                'indexes': [],
                'verbose_name_plural': 'AngularJS Toolbar Foundation',
                'proxy': True,
                'verbose_name': 'AngularJS Toolbar Foundation',
            },
            bases=('krogoth_core.akfoundationabstract',),
        ),
    ]
