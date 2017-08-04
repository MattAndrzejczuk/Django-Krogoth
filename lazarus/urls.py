from django.conf.urls import url
from lazarus import views
from lazarus.views import DependenciesForUnitFBI

urlpatterns = [


    # url(r'^listWorkingDirectory/$', views.listWorkingDirectory.as_view(), name='listWorkingDirectory'),
    url(r'^main/$', views.CustomHtmlGenerator.as_view(), name='index'),
    url(r'^gettheme/$', views.ThemeConstantConfigView.as_view(), name='custom theme'),
    # url(r'^convert_to_png', views.convertPcxToPng.as_view(), name='convertPcxToPng'),
    url(r'^DependenciesForUnitFBI/', DependenciesForUnitFBI.as_view(), name='Dependencies For Unit FBI'),

    # url(r'^ram/$', views.getRam.as_view(), name='ram'),
    # url(r'^processes/$', views.getProcesses.as_view(), name='processes'),
    # url(r'^processesDummy/$', views.getProcessesDummy.as_view(), name='processesDummy'),
    # url(r'^storage/$', views.getStorage.as_view(), name='storage'),
    # url(r'^cpuinfo/$', views.getCPUInfo.as_view(), name='cpuinfo'),
    # url(r'^uptime/$', views.getUpTime.as_view(), name='uptime'),
# getProcessesDummy
]

