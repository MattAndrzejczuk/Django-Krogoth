# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-20 06:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KrogothGantryCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='KrogothGantryDirective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('title', models.CharField(default='Untitled krogoth_gantry Directive', help_text='Cosmetic display name for this directive in the primary navigation view', max_length=55)),
                ('directive_js', models.TextField(default="(function ()\n{\n\t'use strict';\n\tangular\n\t\t.module('app.FUSE_APP_NAME')\n\t\t.directive('_DJANGULAR_DIRECTIVE_NAME_', _DJANGULAR_DIRECTIVE_NAME_Directive);\n\t/** @ngInject */\n\tfunction _DJANGULAR_DIRECTIVE_NAME_Directive()\n\t{\n\t\treturn {restrict: 'AE', replace: 'true', template: '_DJANGULAR_DIRECTIVE_TITLE_'};\n\n\t}})\n();")),
            ],
        ),
        migrations.CreateModel(
            name='KrogothGantryIcon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('code', models.CharField(max_length=75, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='KrogothGantryMasterViewController',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('title', models.CharField(default='Untitled krogoth_gantry Application', help_text='Cosmetic display name for this app in the primary navigation view', max_length=55)),
                ('module_js', models.TextField(default="(function ()\n{\n\t'use strict';\n\tangular.module('app.FUSE_APP_NAME', ['flow']).config(config);\n\n\tfunction config($stateProvider, $translatePartialLoaderProvider, msApiProvider, msNavigationServiceProvider) {\n\t$stateProvider\n\t.state('app.FUSE_APP_NAME', {\n\t\turl: '/FUSE_APP_NAME',\n\t\tviews: {\n\t\t\t'content@app': {\n\t\t\t\ttemplateUrl: '/krogoth_gantry/DynamicHTMLInjector/?name=FUSE_APP_NAME',\n\t\t\t\tcontroller: 'FUSE_APP_NAMEController as vm'\n\t\t\t}\n\t\t}\n\t})\n\t_DJANGULAR_SLAVE_VC_INJECTION_POINT_; /* krogoth_gantry Slave VCs automatically injected here. */\n\t_DJANGULAR_SLAVE_MSAPI_INJECTION_POINT_\n\tmsNavigationServiceProvider.saveItem('NAV_HEADER.FUSE_APP_NAME', {\n\t\ttitle: 'FUSE_APP_TITLE',\n\t\ticon: 'FUSE_APP_ICON',\n\t\tstate: 'app.FUSE_APP_NAME',\n\t\tweight: 3\n\t});  _DJANGULAR_SLAVE_NAV_SERVICE_INJECTIONS_\n\t}\n})();")),
                ('controller_js', models.TextField(default="(function ()\n{\n\t'use strict';\n\tangular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);\n\tfunction FUSE_APP_NAMEController()\n\t{\n\t\t\tvar vm = this;\n\t\t\t vm.viewName = 'FUSE_APP_NAME';\n\t}\n})();")),
                ('view_html', models.TextField(default='<h1>{{ vm.viewName }}</h1>')),
                ('style_css', models.TextField(default='')),
                ('is_enabled', models.BooleanField(default=True, help_text='When disabled, this javascript code and html code will not be loaded.')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krogoth_gantry.KrogothGantryCategory')),
                ('djangular_directive', models.ManyToManyField(blank=True, null=True, to='krogoth_gantry.KrogothGantryDirective')),
            ],
        ),
        migrations.CreateModel(
            name='KrogothGantryService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('title', models.CharField(default='Untitled krogoth_gantry Service', help_text='Cosmetic display name for this service in the primary navigation view', max_length=55)),
                ('service_js', models.TextField(default="(function ()\n{\n\t'use strict';\n\tangular\n\t\t.module('app.FUSE_APP_NAME')\n\t\t.factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);\n\t/** @ngInject */\n\tfunction _DJANGULAR_SERVICE_NAME_($log)\n\t{\n\t\t$log.log('Hello. The service _DJANGULAR_SERVICE_NAME_ is online ! ! !');\n\n\t\tvar service = {\n\t\t\ttestThisService: testThisService\n\t\t};\n\nfunction testThisService()\n\t\t{\n\t\t\t$log.log('_DJANGULAR_SERVICE_NAME_ is working properly.');\n\t\t}\n\t\treturn service;\n\t}\n})();")),
            ],
        ),
        migrations.CreateModel(
            name='KrogothGantrySlaveViewController',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='MUST BE EXACT NAME OF MASTER VIEW CONTROLLER.', max_length=25, unique=True)),
                ('title', models.CharField(default='sideNav', help_text='The name for this slave VC.', max_length=55)),
                ('controller_js', models.TextField(default="(function ()\n{\n\t'use strict';\n\tangular.module('app.FUSE_APP_NAME').controller('_SLAVE_NAME_Controller', _SLAVE_NAME_Controller);\n\tfunction _SLAVE_NAME_Controller($stateParams, $log)\n\t{\n\t\t\tvar vm = this;\n\t\t\t vm.viewName = '_SLAVE_NAME_' + $stateParams.id;\n\t}\n})();")),
                ('view_html', models.TextField(default='<h1>{{ vm.viewName }}</h1>')),
            ],
        ),
        migrations.AddField(
            model_name='krogothgantrymasterviewcontroller',
            name='djangular_service',
            field=models.ManyToManyField(blank=True, null=True, to='krogoth_gantry.KrogothGantryService'),
        ),
        migrations.AddField(
            model_name='krogothgantrymasterviewcontroller',
            name='djangular_slave_vc',
            field=models.ManyToManyField(blank=True, null=True, to='krogoth_gantry.KrogothGantrySlaveViewController'),
        ),
        migrations.AddField(
            model_name='krogothgantrymasterviewcontroller',
            name='icon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krogoth_gantry.KrogothGantryIcon'),
        ),
    ]
