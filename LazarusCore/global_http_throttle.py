from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle


class UploadPerDayUserThrottle(UserRateThrottle):
    rate = '75/day'