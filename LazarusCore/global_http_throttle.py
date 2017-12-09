from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle


class ManualWorkerDispatchThrottle(UserRateThrottle):
    throttle_scope = 'manual_worker'
    rate = '10/min'


class UploadPerDayUserThrottle(UserRateThrottle):
    throttle_scope = 'uploads'
    rate = '75/day'