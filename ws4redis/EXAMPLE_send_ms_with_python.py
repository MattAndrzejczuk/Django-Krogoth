# Author - Matt Andrzejczuk
from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage

welcome = RedisMessage('{"event":"messageType","data":"Hello everybody"}')
pub = RedisPublisher(facility='Socket_Only|Socket_Only#Socket_Only', broadcast=True)
pub._system_message = True
pub.publish_message(welcome)