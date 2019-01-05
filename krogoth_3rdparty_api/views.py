from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from krogoth_3rdparty_api.models import BaseCallbackEndpoint
import json
# Create your views here.

class GenericCallbackURIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        params = request.query_params
        record_of_this = BaseCallbackEndpoint(full_uri=request.build_absolute_uri(), uri_request_params=params)
        record_of_this.save()
        css = "<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css'/>"
        json_dump = json.dumps(params, indent=2, sort_keys=True)
        print(json_dump)
        htmlText = "<br/><p>URI:</p><p>"+ request.build_absolute_uri()+"</p><br/><textarea>" + json_dump + \
                   "</textarea>"
        return HttpResponse(css + '<h1>API Callback</h1>' + htmlText)