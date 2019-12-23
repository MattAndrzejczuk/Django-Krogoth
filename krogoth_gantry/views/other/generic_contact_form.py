from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.views import APIView
from krogoth_gantry.models.generic_contact_form import GenericContactForm

CONTENT_TYPE = 'application/json; charset=utf-8'


class GenericContactViewCreate(APIView):
    authentication_classes = (AllowAny,)

    def post(self, request, format=None):

        title = request.data["title"]
        sender = request.data["sender"]
        body = request.data["body"]

        newModel = GenericContactForm()
        newModel.title = title
        newModel.sender = sender
        newModel.body = body
        newModel.save()
        return JsonResponse({"result": "SUCCESS"}, content_type=CONTENT_TYPE, safe=False)


class GenericContactViewListAll(APIView):
    authentication_classes = (IsAdminUser,)

    def get(self, request, format=None):

        forms = GenericContactForm.objects.all().order_by('-pub_date')
        response = {'items': []}
        for form in forms:
            element = {}
            element['title'] = form.title
            element['pub_date'] = form.pub_date
            element['sender'] = form.sender
            element['id'] = form.id
            element['was_read'] = form.was_read
            element['is_hidden'] = form.is_hidden
            response['items'].append(element)

        return JsonResponse(response, content_type=CONTENT_TYPE, safe=False)


class GenericContactViewDetail(APIView):
    authentication_classes = (IsAdminUser,)

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id', '-1')
        obj = GenericContactForm.objects.get(id=id)
        element = {}
        element['title'] = obj.title
        element['pub_date'] = obj.pub_date
        element['sender'] = obj.sender
        element['id'] = obj.id
        element['body'] = obj.body
        obj.was_read = True
        obj.save()
        return JsonResponse(element, content_type=CONTENT_TYPE, safe=False)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get('id', '-1')
        obj = GenericContactForm.objects.get(id=id)
        obj.is_hidden = True
        obj.save()
        return JsonResponse({"result":"SUCCESS"}, content_type=CONTENT_TYPE, safe=False)
