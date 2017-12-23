from django.conf import settings
from ws4redis.redis_store import RedisStore, SELF
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class RedisSubscriber(RedisStore):
    """
    Subscriber class, used by the websocket code to listen for subscribed channels
    """
    subscription_channels = ['subscribe-session', 'subscribe-group', 'subscribe-user', 'subscribe-broadcast', 'subscribe-count']
    publish_channels = ['publish-session', 'publish-group', 'publish-user', 'publish-broadcast', 'publish-count']

    def __init__(self, connection):
        self._subscription = None
        super(RedisSubscriber, self).__init__(connection)



    def parse_response(self):
        """
        Parse a message response sent by the Redis datastore on a subscribed channel.
        """

        return self._subscription.parse_response()

    def clean_up_response(self, raw_sndmsg):
        """
        Listen for messages on channels this client has been subscribed to
        """
        r = []
        for i in raw_sndmsg:
            if isinstance(i, bytes):
                r.append(i.decode('utf8'))
            else:
                r.append(i)

        if r[0] == 'pmessage':
            msg = {
                'type': r[0],
                'pattern': r[1],
                'channel': r[2],
                'data': r[3]
            }
        else:
            msg = {
                'type': r[0],
                'pattern': None,
                'channel': r[1],
                'data': r[2]
            }
        return msg

        # return self._subscription.listen()

    def set_pubsub_channels(self, request: WSGIRequest, channels):
        """
        Initialize the channels used for publishing and subscribing messages through the message queue.

        A facility looks like:                     US~CA#General
        Using the example above, a region is:      US~CA
        and the corresponding chatroom is          #General


        """
        facility = request.path_info.replace(settings.WEBSOCKET_URL, '', 1)

        prefix = self.get_prefix()

        region = facility.split('#')[0]

        chat_room = facility.split('#')[1]

        print(region)

        username = 'guest'
        try:
            request.user = User.objects.get(id=Token.objects.get(key=request.COOKIES['token']).user_id)
            username = request.user.username
        except:
            print('\033[92m' + ' NOT AUTHENTICATED! cookie with key "token" is not authenticated.' + '\033[0m')
            print(request.user)
            print('\033[95m')
            print(request.COOKIES)
        print(username + " has entered " + str(facility))
        print('\033[0m')



        # initialize publishers
        audience = {
            'users': 'publish-user' in channels and [SELF] or [],
            'groups': 'publish-group' in channels and [SELF] or [],
            'sessions': 'publish-session' in channels and [SELF] or [],
            'broadcast': 'publish-broadcast' in channels,
        }
        self._publishers = set()
        for key in self._get_message_channels(request=request, facility=facility, **audience):
            self._publishers.add(key)

        # initialize subscribers
        audience = {
            'users': 'subscribe-user' in channels and [SELF] or [],
            'groups': 'subscribe-group' in channels and [SELF] or [],
            'sessions': 'subscribe-session' in channels and [SELF] or [],
            'broadcast': 'subscribe-broadcast' in channels,
        }
        self._subscription = self._connection.pubsub()
        print(audience)
        ### SUBSCRIBE TO THE CURRENT REGIONS CHATROOMS ONLY TO GET INFORMATION ON CHATROOMS
        ### FOR NOW, I WILL ONLY SEND THE CLIENT LIST OF PEOPLE PER CHATROOM IN REAL TIME

        ## for chatroom in self._subscription.keys('demo:broadcast:US~CA#*:chatroom'):
        ##      subscribe to all keys in this loop
        self._subscription.subscribe('{prefix}broadcast:{facility}:chatroom'.format(prefix=prefix, facility=facility))
        for key in self._get_message_channels(request=request, facility=facility, **audience):
            print(key)
            self._subscription.psubscribe('*' + key + '*')
            self._subscription.subscribe(key)

    def send_persited_messages(self, websocket):
        """
        This method is called immediately after a websocket is openend by the client, so that
        persisted messages can be sent back to the client upon connection.
        """
        for channel in self._subscription.channels:
            message = self._connection.get(channel)
            if message:
                websocket.send(message)

    def get_file_descriptor(self):
        """
        Returns the file descriptor used for passing to the select call when listening
        on the message queue.
        """
        return self._subscription.connection and self._subscription.connection._sock.fileno()

    def release(self, request):
        """
        New implementation to free up Redis subscriptions when websockets close. This prevents
        memory sap when Redis Output Buffer and Output Lists build when websockets are abandoned.
        """
        print('guest' + " has left the channel.")
        if self._subscription and self._subscription.subscribed:
            self._subscription.unsubscribe()
            self._subscription.reset()
