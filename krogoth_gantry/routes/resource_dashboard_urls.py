from django.conf.urls import url
from krogoth_gantry.views import resource_dashboard

urlpatterns = [
    url(r'^ram/$', resource_dashboard.getRam.as_view(), name='ram'),
    url(r'^processes/$', resource_dashboard.getProcesses.as_view(), name='processes'),
    url(r'^processesDummy/$', resource_dashboard.getProcessesDummy.as_view(), name='processesDummy'),
    url(r'^storage/$', resource_dashboard.getStorage.as_view(), name='processes'),
    url(r'^cpuinfo/$', resource_dashboard.getCPUInfo.as_view(), name='processes'),
    url(r'^uptime/$', resource_dashboard.getUpTime.as_view(), name='processes'),
]
