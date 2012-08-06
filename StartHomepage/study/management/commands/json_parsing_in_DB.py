import json, requests, urllib2, urllib
from django.core.management.base import NoArgsCommand
from study.models import *
from django.core import serializers

def input():
    url_m = "http://openapi.seoul.go.kr:8088/json/4150495f3230383363686c6475713034/%EC%A0%84%ED%86%B5%EC%8B%9C%EC%9E%A5%20%EC%A0%95%EB%B3%B4/1/50/" 
    rm = json.loads(requests.get(url_m).content.decode("utf-8"))
    entry = goo_map.objects.all()
    lat_m = []    
    for i,k in rm.iteritems():
        for l,m in k.iteritems():
            mTitle = m[u'M_NAME']
            m_address = m[u'M_ADDR']
            check = True
            for item in entry:
                if item.Title == mTitle:
                    check = False
                    break

            if check == True:
                parse = urllib.urlencode({'address':m_address.encode('utf-8'),'sensor':'false','language':'ko'}) 
                go_url = urllib2.urlopen('http://maps.googleapis.com/maps/api/geocode/json?%s' % parse);
                road_map = json.loads(go_url.read(),encoding='utf-8')
                if road_map['status'] == 'OK' :
                    new_entry = goo_map(Title=m[u'M_NAME'], Content=m[u'M_SUBWAY'],Addr_X=road_map['results'][0]['geometry']['location']['lat'],Addr_Y=road_map['results'][0]['geometry']['location']['lng'], mAddr=m[u'M_ADDR'])
               
                try:
                    new_entry.save()
                    print ('Success!!!')             
                except:
                    print('Error..or not enough information'+mTitle)
            else:
                print("already exist")    
            #lat_m.append((m[u'M_SUBWAY'],m[u'M_NAME'],m[u'M_PARKING'],m[u'M_ADDR']))
    
    
    q = goo_map.objects.all()
    for i in q:
        print i.Title

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        input()

        
