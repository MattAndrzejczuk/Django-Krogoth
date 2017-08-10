from django.db import models
from polymorphic.models import PolymorphicModel
from django.contrib.auth.models import User
import json
from urllib.request import urlopen
from django.contrib.postgres.fields import JSONField
# Create your models here.
class JawnUser(models.Model):
    base_user = models.OneToOneField(User, related_name='jawn_user', )
    profile_pic = models.ImageField(upload_to="media/", blank=True, null=True)
    about_me = models.CharField(max_length=400, blank=True, null=True)
    follows = models.ManyToManyField('self', related_name='followers', symmetrical=False, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    SIDES = (
        ('core', 'Core'),
        ('arm', 'Arm'),
    )
    faction = models.CharField(choices=SIDES, null=True, blank=True, max_length=10)

    def __str__(self):
        return self.base_user.username


class Channel(models.Model):
    name = models.CharField(max_length=400, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(JawnUser, related_name='creator', blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    description = models.TextField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.name


class Message(PolymorphicModel):
    date_posted = models.DateTimeField(auto_now_add=True)
    jawn_user = models.ForeignKey(JawnUser, related_name='user', blank=True, null=True)
    channel = models.ForeignKey(Channel, related_name='messages')


class ImageMessage(Message):
    CHOICES = (('image', 'image'),)
    type = models.CharField(max_length=50, default='image', choices=CHOICES)
    image_url = models.ImageField(upload_to='media/')
    caption = models.TextField(max_length=1000, blank=True, null=True)


class TextMessage(Message):
    CHOICES = (('text', 'text'),)
    type = models.CharField(max_length=50, default='text', choices=CHOICES)
    text = models.TextField(max_length=1000)



class LinkMessage(Message):
    CHOICES = (('link', 'link'),)
    type = models.CharField(max_length=50, default='link', choices=CHOICES)
    text = models.TextField(max_length=1000)
    image_url = models.URLField(null=True, blank=True)
    headline = models.CharField(max_length=250)
    organization = models.CharField(max_length=250)
    
    
class YouTubeMessage(Message):
    CHOICES = (('youtube', 'youtube'),)
    type = models.CharField(max_length=50, default='youtube', choices=CHOICES)
    text = models.TextField(max_length=1000)
    youtube_url = models.URLField(null=True, blank=True)
    youtube_id = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    

class RegionManager(models.Manager):
    def create_region(self, **kwargs):
        js = kwargs['google_json']
        njs = json.loads(js)
        kwargs['google_json'] = njs
        #print(kwargs['google_json']['geometry']['location']['lat'])
        #print(kwargs['google_json']['geometry']['location']['lng'])
        typeAndLongName = [kwargs['google_json']['types'][0], kwargs['google_json']['long_name'][0]]
        flickr = get_flickr_url(lat=kwargs['google_json']['geometry']['location']['lat'], long=kwargs['google_json']['geometry']['location']['lng'], type=typeAndLongName)
        kwargs['flickr_image'] = flickr['flickrURL']
        kwargs['flickr_image_large'] = flickr['flickrURLLarge']
        #print(kwargs)
        region = self.create(**kwargs)
        return region



class Region(models.Model):
    name = models.CharField(max_length=150)
    coordinates_long = models.FloatField()
    coordinates_lat = models.FloatField()
    flickr_image = models.CharField(max_length=150, null=True)
    flickr_image_large = models.CharField(max_length=150, null=True)
    google_json = JSONField()


    objects = RegionManager()


    # @classmethod
    # def save(self):
    #     # Run logic when a new object is created.
    #     self.flickr_image = "IT WORKS!"# self.get_flickr_image(lat, long)
    #     self.save()
    #     print(self)
    #     print(dir(self))
    #     return Super(Region, self).save(self)


class PrivateMessageRelationships(models.Model):
    channel = models.OneToOneField(Channel, related_name='channel', )
    user_recipient = models.ForeignKey(User, related_name='user_recipient', )
    user_sender = models.ForeignKey(User, related_name='user_sender', )
    channel_name = models.CharField(max_length=150) # may need to remove this later.


def get_flickr_url(lat, long, type, accuracy='11'):
    url_ = 'https://api.flickr.com/services/rest/?method=flickr.photos.search'
    API_key = '7d246b0b6518d209b4cde09e0d485832'
    format_ = 'json&nojsoncallback=1'
    text_ = type[0]
    lat_ = lat
    long_ = long
    accuracy_ = accuracy
    #strurl = url_+'&api_key='+API_key+'&tags='+text_+'&lat='+str(lat_)+'&lon='+str(long_)+'&format='+format_+'&accuracy='+accuracy_+'&tag_mode=any'+'&in_gallery=1&content_type=1'

    if "administrative_area_level_1" in text_:
        long_ += 1
        lat_ -= 2
        text_ = 'sunset,hill,skyline,landmark'
    elif "country" in text_:
        long_ -= 2
        lat_ -= 1
        text_ = 'nature,patriot,beautiful,country'
    elif 'administrative_area_level_2' in text_:
        long_ -= 1
        lat_ += 1
        text_ = 'city,urban,skyline,downtown'
    elif "sublocality" in text_:
        long_ += 2
        lat_ -= 2
        text_ = 'street,metro,park,home'
    elif "locality" in text_:
        long_ += 4
        lat_ -= 4
        text_ = 'street,metro,park'
    elif "neighborhood" in text_:
        long_ += 1
        lat_ += 1
        text_ = 'house,neighborhood'
    else:
        text_ = 'clouds'

    print('#####################')
    print('#####################')
    print(text_)
    print('#####################')
    print('#####################')

    strurl = url_+'&api_key='+API_key+'&tags='+text_+'&lat='+str(lat_)+'&lon='+str(long_)+'&format='+format_+'&accuracy='+accuracy_+'&tag_mode=any'+'&in_gallery=1&content_type=1'

    i = -1
    
    
    flickrImageID = ''
    while i < 6:
        i = i + 1
        request = urlopen(strurl)
        response = request.read().decode("utf-8")
        data = json.loads(response)
        pic = 0
        #dummy https://domfa.de/get_image/?text=niceview&lat=37.4451198&long=-122.1561692
        try:
            #print(data)
            #print(i)
            farm_id = str(data['photos']['photo'][i]['farm'])
            server_id = str(data['photos']['photo'][i]['server'])
            image_id = str(data['photos']['photo'][i]['id'])
            image_secret = str(data['photos']['photo'][i]['secret'])
            flickrImageID = image_id
        except IndexError:
            #if "aerial" in text_:
            #if lat_ == '{$num_lat$}':
            #    text_ = 'outdoors'
            long_ += 1
            lat_ -= 1
            
            """
            print('THE EXCEPTION HAS BEEN TRIGGERED!')
            print('THE EXCEPTION HAS BEEN TRIGGERED!')
            print('THE EXCEPTION HAS BEEN TRIGGERED!')
            print('THE EXCEPTION HAS BEEN TRIGGERED!')
            print(data)
            print('THE EXCEPTION HAS BEEN TRIGGERED!')
            print('THE EXCEPTION HAS BEEN TRIGGERED!')
            print('THE EXCEPTION HAS BEEN TRIGGERED!')
            print('THE EXCEPTION HAS BEEN TRIGGERED!')
            """
            text_=''
            strurl = url_+'&api_key='+API_key+'&tags='+text_+'&format='+format_
            request = urlopen(strurl)
            response = request.read().decode("utf-8")
            data = json.loads(response)
            """
            print('EXCEPTION TRIGGERED AGAIN!!!')
            print('EXCEPTION TRIGGERED AGAIN!!!')
            print('EXCEPTION TRIGGERED AGAIN!!!')
            print(data)
            print('EXCEPTION TRIGGERED AGAIN!!!')
            print('EXCEPTION TRIGGERED AGAIN!!!')
            print('EXCEPTION TRIGGERED AGAIN!!!')
            """
            #print(response)
            #print(data)
            farm_id = str(data['photos']['photo'][i]['farm'])
            server_id = str(data['photos']['photo'][i]['server'])
            image_id = str(data['photos']['photo'][i]['id'])
            image_secret = str(data['photos']['photo'][i]['secret'])
        flickrURL = 'https://farm'+farm_id+'.staticflickr.com/'+server_id+'/'+image_id+'_'+image_secret+'.jpg'
        #print(flickrURL)
        
        returnValue = {"flickrURL":flickrURL, "flickrURLLarge":get_flickr_url_large(flickrImageID)}
        
        #return flickrURL <-Legacy Version, Uncomment to activate
        return returnValue
    
    
    
def get_flickr_url_large(flickrImageID):
    API_key = '7d246b0b6518d209b4cde09e0d485832'
    largestImage = 'FAIL' # default if there's no return value.
    url_2 = 'https://api.flickr.com/services/rest/?method=flickr.photos.getSizes'  
    imgID_2 = flickrImageID
    fullURL = url_2 +'&api_key='+API_key+'&photo_id='+imgID_2+'&format=json&nojsoncallback=1'
    request = urlopen(fullURL)
    response = request.read().decode("utf-8")
    data2 = json.loads(response)   
    allSizes = data2['sizes']['size']
     
    for size in allSizes:
        if size['label'] != 'Original':
            largestImage = size['source']
    return largestImage
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    