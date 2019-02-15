from krogoth_3rdparty_api.models import BaseCallbackEndpoint
import twitter
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from krogoth_3rdparty_api.models import BaseCallbackEndpoint
import json

"""
        api.PostUpdates(status)
        api.PostDirectMessage(user, text)
        api.GetUser(user)
        api.GetReplies()
        api.GetUserTimeline(user)
        api.GetHomeTimeline()
        api.GetStatus(status_id)
        api.DestroyStatus(status_id)
        api.GetFriends(user)
        api.GetFollowers()
        api.GetFeatured()
        api.GetDirectMessages()
        api.GetSentDirectMessages()
        api.PostDirectMessage(user, text)
        api.DestroyDirectMessage(message_id)
        api.DestroyFriendship(user)
        api.CreateFriendship(user)
        api.LookupFriendship(user)
        api.VerifyCredentials()
"""
# Create your views here.

class UserTimelineTest(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        params = request.query_params
        # record_of_this = BaseCallbackEndpoint(full_uri=request.build_absolute_uri(), uri_request_params=params)
        # record_of_this.save()
        css = "<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css'/>"
        json_dump = json.dumps(params, indent=2, sort_keys=True)
        print(json_dump)
        htmlText = "<br/><p>URI:</p><p>" + request.build_absolute_uri() + "</p><br/><textarea>" + json_dump + \
                   "</textarea><br/>"
        k1 = '0YlLSyFd1IjPOjMO4USWLdBNi'
        k2 = 'II8adw2j1Uauo9goxTtGg7srJApsHxBwG4pvjpKr6e3B01sIBJ'
        atk = "783776659732168704-gZVXLb6MbGBXzONyQPXeA0l92NyPIYL"
        ats = "gOZF8O7jTnMvJOAWovctqSFEyraVJH5UIfk949YYjKz4T"

        api = twitter.Api(consumer_key=k1, consumer_secret=k2, access_token_key=atk, access_token_secret=ats)

        timeline = api.GetUserTimeline(screen_name='CoreKrogoth',
                                       exclude_replies=True,
                                       include_rts=False, )



        print(timeline)
        return JsonResponse(json.dumps(timeline), safe=False)