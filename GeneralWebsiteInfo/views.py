from django.shortcuts import render
from GeneralWebsiteInfo.models import WebsiteColorTheme, WebsiteLayout, NavigationBar, BootScreenLoader


from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response



# GeneralWebsiteInfo

###   WebsiteColorThemeView
###   WebsiteLayoutView
###   NavigationBarView
###   BootScreenLoaderView




class WebsiteColorThemeView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        name = str(request.GET['name'])
        try:
            html_view = WebsiteColorTheme.objects.get(name=name)
            return HttpResponse(html_view.contents)
        except:
            html = '<div> <h1>Fatal Error</h1> <p>Unable to load HTML: <b>' + name + '</b> </p> </div>'
            return HttpResponse(html)

class WebsiteLayoutView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        name = str(request.GET['name'])

        try:
            html_view = WebsiteLayout.objects.get(name=name)
            return HttpResponse(html_view.contents)
        except:
            html = '<div> <h1>Fatal Error</h1> <p>Unable to load HTML: <b>' + name + '</b> </p> </div>'
            return HttpResponse(html)

class NavigationBarView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        name = str(request.GET['name'])

        try:
            html_view = NavigationBar.objects.get(name=name)
            return HttpResponse(html_view.contents)
        except:
            html = '<div> <h1>Fatal Error</h1> <p>Unable to load HTML: <b>' + name + '</b> </p> </div>'
            return HttpResponse(html)

class BootScreenLoaderView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        name = str(request.GET['name'])

        try:
            html_view = BootScreenLoader.objects.get(name=name)
            return HttpResponse(html_view.contents)
        except:
            html = '<div> <h1>Fatal Error</h1> <p>Unable to load HTML: <b>' + name + '</b> </p> </div>'
            return HttpResponse(html)


class PressArticleListView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        try:
            articles = PressArticle.objects.all()
            list = []
            for art in articles:
                json_obj = {}
                json_obj['title'] = art.title
                json_obj['author'] = art.author
                json_obj['pub_date'] = art.pub_date
                json_obj['body'] = art.body
                list.append(json_obj)
            return Response(list)
        except:
            return Response('', status=404)


class PressArticleView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        try:
            id = str(request.GET['id'])
            article = PressArticle.objects.get(id=id)
            json_response = {
                'title':article.title,
                'author': article.author.username,
                'pub_date':article.pub_date,
                'body':article.body
            }
            return Response(json_response, status=404)
        except:
            return Response('', status=404)

    def post(self, request, *args, **kwargs):
        title = str(request.POST['title'])
        body = str(request.POST['body'])

        new_article = PressArticle()
        new_article.title = title
        new_article.body = body
        new_article.author = request.user
        new_article.save()
        json_response = {
            'title':new_article.title,
            'author': new_article.author.username,
            'pub_date':new_article.pub_date,
            'body':new_article.body
        }
        return Response(json_response, status=201)

    def put(self, request, *args, **kwargs):
        id = str(request.POST['id'])
        title = str(request.POST['title'])
        body = str(request.POST['body'])
        try:
            new_article = PressArticle.objects.get(id=id)
            new_article.title = title
            new_article.body = body
            new_article.author = request.user

            new_article.save()

            json_response = {
                'title': new_article.title,
                'author': new_article.author.username,
                'pub_date': new_article.pub_date,
                'body': new_article.body
            }
            return Response(json_response, status=204)
        except:
            return Response('', status=404)

    def delete(self, request, *args, **kwargs):
        id = str(request.POST['id'])
        try:
            article = PressArticle.objects.get(id=id)
            article.delete()
            return Response(json_response, status=200)
        except:
            return Response(json_response, status=404)
