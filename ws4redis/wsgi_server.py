import sys
import six
from six.moves import http_client
from redis import StrictRedis
import django
if django.VERSION[:2] >= (1, 7):
    django.setup()
from django.conf import settings
from django.contrib.auth import get_user
from django.core.handlers.wsgi import WSGIRequest
from django.core.exceptions import PermissionDenied
from django import http
from django.utils.encoding import force_str
from django.utils.functional import SimpleLazyObject
from ws4redis import settings as private_settings
from ws4redis.redis_store import RedisMessage
from ws4redis.exceptions import WebSocketError, HandshakeError, UpgradeRequiredError
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import datetime
import json
import time
import logging






class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    TEAL = '\033[96m'
    BLACK = '\033[97m'
    GRAY = '\033[90m'
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'


def log1(p):
    print(bcolors.purple, end=" ")
    print(p, end=" 1 ")
    print(bcolors.ENDC, end=" ")

def log2(p):
    print(bcolors.blue, end=" ")
    print(p, end=" 2 ")
    print(bcolors.ENDC, end=" ")

def log3(p):
    print(bcolors.yellow, end=" ")
    print(p, end=" 3 ")
    print(bcolors.ENDC, end=" ")

def log4(p):
    print(bcolors.purple, end=" ")
    print(p, end=" 4 ")
    print(bcolors.ENDC, end=" ")


def log5(p):
    print(bcolors.TEAL, end=" ")
    print(p, end=" 5 ")
    print(bcolors.ENDC, end=" ")


def log6(p):
    print(bcolors.OKGREEN, end=" ")
    print(p, end=" 6 ")
    print(bcolors.ENDC, end=" ")


def log7(p):
    print(bcolors.green, end=" ")
    print(p, end=" 7 ")
    print(bcolors.ENDC, end=" ")


def log8(p):
    print(bcolors.OKBLUE, end=" ")
    print(p, end=" 8 ")
    print(bcolors.ENDC, end=" ")





try:
    # django >= 1.8 && python >= 2.7
    # https://docs.djangoproject.com/en/1.8/releases/1.7/#django-utils-dictconfig-django-utils-importlib
    from importlib import import_module
except ImportError:
    # RemovedInDjango19Warning: django.utils.importlib will be removed in Django 1.9.
    from django.utils.importlib import import_module


class WebsocketWSGIServer(object):
    def __init__(self, redis_connection=None):
        """
        redis_connection can be overriden by a mock object.
        """
        comps = str(private_settings.WS4REDIS_SUBSCRIBER).split('.')
        module = import_module('.'.join(comps[:-1]))
        Subscriber = getattr(module, comps[-1])
        self.possible_channels = Subscriber.subscription_channels + Subscriber.publish_channels
        self._redis_connection = redis_connection and redis_connection or StrictRedis(**private_settings.WS4REDIS_CONNECTION)
        self.Subscriber = Subscriber

    def assure_protocol_requirements(self, environ):
        if environ.get('REQUEST_METHOD') != 'GET':
            raise HandshakeError('HTTP method must be a GET')

        if environ.get('SERVER_PROTOCOL') != 'HTTP/1.1':
            raise HandshakeError('HTTP server protocol must be 1.1')

        if environ.get('HTTP_UPGRADE', '').lower() != 'websocket':
            raise HandshakeError('Client does not wish to upgrade to a websocket')

    def process_request(self, request):
        """
        NEED TO SET UP A SECURE WAY TO HANDLE REQUESTS THAT DONT HAVE AN ACCESS TOKEN
        :param request:
        :return:
        """
        request.session = None
        request.user = None
        # session_key = request.COOKIES.get(settings.SESSION_COOKIE_NAME, None)
        # if session_key is not None:
        #     # print(session_key)
        #     engine = import_module(settings.SESSION_ENGINE)
        #     request.session = engine.SessionStore(session_key)
        #     # session = Session.objects.get(session_key=session_key)
        #     request.user = SimpleLazyObject(lambda: get_user(request))
        # if 'Token' in request.META['REQUEST_URI']:
        #     token = request.META['REQUEST_URI'].split('Token', 1)[1]
        #     request.user = json.loads(self._redis_connection.get('tokens:' + token).decode('utf8'))
        #     print(request.user)


        # get user by using the request token:
        # if request.META['HTTP_AUTHORIZATION']:
        #     print(request.META['HTTP_AUTHORIZATION'])
        #     a = request.META['HTTP_AUTHORIZATION']
        #     array = a.split()
        #     token = array[1]
        #     print(token)
        #     print(self._redis_connection)
        #     request.user = json.loads(self._redis_connection.get('tokens:' + token).decode('utf8'))

            # request.user = User.objects.get(id=Token.objects.get(key=token).user_id)
            # print(request.user)


    def process_subscriptions(self, request):
        agreed_channels = []
        echo_message = False
        for qp in request.GET:
            param = qp.strip().lower()
            if param in self.possible_channels:
                agreed_channels.append(param)
            elif param == 'echo':
                echo_message = True
        return agreed_channels, echo_message

    def __call__(self, environ, start_response):
        """
        Hijack the main loop from the original thread and listen on events on the Redis
        and the Websocket filedescriptors.
        """
        websocket = None
        subscriber = self.Subscriber(self._redis_connection)
        try:
            self.assure_protocol_requirements(environ)
            request = WSGIRequest(environ)
            if callable(private_settings.WS4REDIS_PROCESS_REQUEST):
                private_settings.WS4REDIS_PROCESS_REQUEST(request)
            else:
                self.process_request(request)
            channels, echo_message = self.process_subscriptions(request)
            if callable(private_settings.WS4REDIS_ALLOWED_CHANNELS):
                channels = list(private_settings.WS4REDIS_ALLOWED_CHANNELS(request, channels))
            elif private_settings.WS4REDIS_ALLOWED_CHANNELS is not None:
                try:
                    mod, callback = private_settings.WS4REDIS_ALLOWED_CHANNELS.rsplit('.', 1)
                    callback = getattr(import_module(mod), callback, None)
                    if callable(callback):
                        channels = list(callback(request, channels))
                except AttributeError:
                    pass
            websocket = self.upgrade_websocket(environ, start_response)
            log1('Subscribed to channels: {0}'.format(', '.join(channels)))

            subscriber.set_pubsub_channels(request, channels)
            websocket_fd = websocket.get_file_descriptor()
            listening_fds = [websocket_fd]
            redis_fd = subscriber.get_file_descriptor()
            if redis_fd:
                log3(redis_fd)
                listening_fds.append(redis_fd)
            recvmsg = None
            enter_msg_counter = 0
            while websocket and not websocket.closed:

                ready = self.select(listening_fds, [], [], 4.0)[0]
                if not ready:
                    # flush empty socket
                    websocket.flush()
                for fd in ready:
                    if fd == websocket_fd:
                        recvmsg = RedisMessage(websocket.receive())
                        if recvmsg:
                            log5('recvmsg: ')
                            log6(recvmsg)
                            subscriber.publish_message(recvmsg)
                    elif fd == redis_fd:
                        sendmsg = RedisMessage(subscriber.parse_response())
                        if sendmsg and (echo_message or sendmsg != recvmsg):
                            log7('sendmsg: ')
                            log8(sendmsg)
                            websocket.send(sendmsg)
                    else:
                        log2('Invalid file descriptor: {0}'.format(fd))
                # Check again that the websocket is closed before sending the heartbeat,
                # because the websocket can closed previously in the loop.
                if private_settings.WS4REDIS_HEARTBEAT and not websocket.closed:
                    websocket.send(private_settings.WS4REDIS_HEARTBEAT)
                # Remove websocket from _websockets if closed
                if websocket.closed:
                    self._websockets.remove(websocket)




                # prefix = subscriber.get_prefix()
                # facility = request.path_info.replace(settings.WEBSOCKET_URL, '', 1)
                # if enter_msg_counter == 0:
                #     subscriber.add_user_to_chatroom(request=request)
                #     subscriber.send_persited_messages(websocket)
                #     enter_msg_counter += 1
                # ready = self.select(listening_fds, [], [], 4.0)[0]
                # print(ready)
                # if not ready:
                #     # flush empty socket
                #     websocket.flush()
                # for fd in ready:
                #     # a = RedisMessage(str(list_o_users))
                #     # websocket.send(a)
                #     if fd == websocket_fd:
                #         """
                #         ################
                #         EVERYTHING THIS LOOP HAPPENS WHEN THE WEBSOCKET RECEIVES A MESSAGE
                #         I.E. A CLIENT SENDING SOMETHING UPSTREAM
                #         ################
                #
                #         I need to create a parser here which knows to publish
                #         the correct message into the correct prefix....
                #
                #         i.e. {prefix}:{region}#{channel name}:{type}
                #         type can be: chatroom, typing, text, etc.
                #         """
                #
                #         rec = websocket.receive()
                #         """
                #         the parser should begin here, where we figure out what kind of message this is,
                #         but first we need to weed out the strings from the JSON strings
                #         """
                #         recv_dict = {}
                #         try:
                #             recv_dict = json.loads(rec.decode('utf8'))
                #             print(recv_dict)
                #             recvmsg = None
                #         except ValueError:
                #             recvmsg = RedisMessage(rec)
                #         except TypeError:
                #             recvmsg = RedisMessage(rec)
                #         print(str(recv_dict) + " this is HERE")
                #         # rec_dict = json.loads(recvmsg)
                #         # print(rec_dict)
                #         """
                #         if recvmsg is of type RedisMessage, this means it was
                #         """
                #         if recvmsg:
                #             print(str(recvmsg) + " recvmessage")
                #             subscriber.publish_message(recvmsg)
                #         if recv_dict:
                #             print(recv_dict)
                #             if recv_dict['event'] == 'action':
                #                 if recv_dict['action'] == 'typing':
                #                     print(recv_dict)
                #                     subscriber.user_is_typing(request=request, expiration=3)
                #                     # run some typing method in here
                #                 elif recv_dict['action'] == 'upvote':
                #                     pass
                #                 elif recv_dict['action'] == 'message sent':
                #                     print('typing typing typing typing typing #########################')
                #                     subscriber.user_not_typing(request=request)
                #                     # run upvote method logic here
                #             elif recv_dict['event'] == 'text':
                #                 """
                #                 if client is sending a message upstream as "ephemeral" instead of
                #                 permenantly to the DB
                #                 """
                #                 recv_dict['jawn_user'] = request.user
                #                 message = json.dumps(recv_dict)
                #                 recvmsg = RedisMessage(message)
                #                 subscriber.publish_message(recvmsg)
                #             elif recv_dict['event'] == 'simple':
                #                 """
                #                 if client is sending a message upstream as "ephemeral" instead of
                #                 permenantly to the DB
                #                 """
                #                 # recv_dict['jawn_user'] = request.user
                #                 # message = json.dumps(recv_dict)
                #                 recvmsg = RedisMessage(recv_dict['data'])
                #                 subscriber.publish_message(recvmsg)
                #                 websocket.send(recvmsg)
                #     elif fd == redis_fd:
                #         """
                #         ################
                #         EVERYTHING THIS LOOP HAPPENS WHEN THE REDIS QUEUE RECEIVES A MESSAGE
                #         I.E. A REDIS NOTIFICATION OR PUBSUB EVENT
                #         ################
                #         """
                #         print('SHIT!!')
                #         raw = subscriber.parse_response()
                #         msg = subscriber.clean_up_response(raw)
                #         ### check and see if there is JSON inside msg['data']
                #         try:
                #             # new_dict = json.loads(msg['data'])
                #             # msg['data'] = new_dict
                #             print(msg)
                #         except ValueError:
                #             logging.warning('Got ValueError on when parsing {}'.format(str(msg)), exc_info=sys.exc_info())
                #             pass
                #         except TypeError:
                #             pass
                #             logging.warning('Got TypeError on when parsing {}'.format(str(msg)), exc_info=sys.exc_info())
                #         # if msg['type'] == 'pmessage':
                #         #     new_outgoing_dict = {}
                #         #     new_outgoing_dict['data'] = 'action'
                #         #     if ':typing:' in msg['channel']:
                #         #         user = msg['channel'].split(':typing:', 1)[1]
                #         #         new_outgoing_dict['user'] = user
                #         #         new_outgoing_dict['facility'] = facility
                #         #         new_outgoing_dict['type'] = 'typing'
                #         #         if msg['data'] == 'set':
                #         #             new_outgoing_dict['action'] = 'started'
                #         #             new_outgoing_dict['message'] = user + ' is typing'
                #         #             msg = new_outgoing_dict
                #         #         elif msg['data'] == 'expired' or msg['data'] == 'del':
                #         #             new_outgoing_dict['action'] = 'stopped'
                #         #             new_outgoing_dict['message'] = user + ' stopped typing'
                #         #             msg = new_outgoing_dict
                #         #         elif msg['data'] == 'expire':
                #         #             msg = None
                #         #     elif ':chatroom:' in msg['channel']:
                #         #         user = msg['channel'].split(':chatroom:', 1)[1]
                #         #         new_outgoing_dict['user'] = user
                #         #         new_outgoing_dict['facility'] = facility
                #         #         new_outgoing_dict['type'] = 'chatroom'
                #         #         if msg['data'] == 'set':
                #         #             new_outgoing_dict['action'] = 'joined'
                #         #             new_outgoing_dict['message'] = user + ' has joined the channel'
                #         #             msg = new_outgoing_dict
                #         #         elif msg['data'] == 'expired' or msg['data'] == 'del':
                #         #             new_outgoing_dict['action'] = 'left'
                #         #             new_outgoing_dict['message'] = user + ' has left the channel'
                #         #             msg = new_outgoing_dict
                #         #         elif msg['data'] == 'expire':
                #         #             msg = None
                #         #     elif msg['channel'] == '__keyspace@0__:' + prefix + 'broadcast:' + facility or msg['channel'] == '__keyspace@0__:' + prefix + 'broadcast:' + facility + ':chatroom' or prefix + 'broadcast:' + facility:
                #         #         msg = None
                #         # elif msg['data'] == private_settings.WS4REDIS_HEARTBEAT:
                #         #     msg = None
                #         # m = json.dumps(msg, ensure_ascii=False)
                #
                #         print('THE RAW MESSAGE')
                #         print(raw)
                #         print('THE MSG')
                #         print(msg)
                #
                #         sendmsg = RedisMessage(msg['data'])
                #         if sendmsg and (echo_message or sendmsg != recvmsg):
                #             print(" this is inside the websocket loop (sendmsg)")
                #             websocket.send(sendmsg)
                #     else:
                #         logging.error('Invalid file descriptor: {0}'.format(fd))
                # # Check again that the websocket is closed before sending the heartbeat,
                # # because the websocket can closed previously in the loop.
                # if private_settings.WS4REDIS_HEARTBEAT and not websocket.closed:
                #     websocket.send(private_settings.WS4REDIS_HEARTBEAT)







        except WebSocketError as excpt:
            logging.warning('WebSocketError: {}'.format(excpt), exc_info=sys.exc_info())
            response = http.HttpResponse(status=1001, content='Websocket Closed')
        except UpgradeRequiredError as excpt:
            logging.info('Websocket upgrade required')
            response = http.HttpResponseBadRequest(status=426, content=excpt)
        except HandshakeError as excpt:
            logging.warning('HandshakeError: {}'.format(excpt), exc_info=sys.exc_info())
            response = http.HttpResponseBadRequest(content=excpt)
        except PermissionDenied as excpt:
            logging.warning('PermissionDenied: {}'.format(excpt), exc_info=sys.exc_info())
            response = http.HttpResponseForbidden(content=excpt)
        except Exception as excpt:
            logging.error('Other Exception: {}'.format(excpt), exc_info=sys.exc_info())
            response = http.HttpResponseServerError(content=excpt)
        else:
            response = http.HttpResponse()
        finally:
            subscriber.remove_user_from_chatroom(request=request)
            subscriber.release(request)
            if websocket:
                websocket.close(code=1001, message='Websocket Closed')
            else:
                logging.warning('Starting late response on websocket')
                status_text = http_client.responses.get(response.status_code, 'UNKNOWN STATUS CODE')
                status = '{0} {1}'.format(response.status_code, status_text)
                headers = response._headers.values()
                if six.PY3:
                    headers = list(headers)
                start_response(force_str(status), headers)
                logging.info('Finish non-websocket response with status code: {}'.format(response.status_code))
        return response
