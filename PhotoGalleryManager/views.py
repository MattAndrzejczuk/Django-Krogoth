from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response



class ScaffoldView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        html = '<div> <h1>It works!!!</h1> <p> Nothing to see here </p> </div>'
        return HttpResponse(html)

