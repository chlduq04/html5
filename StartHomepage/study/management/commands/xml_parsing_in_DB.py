import json, requests, urllib2, urllib
from xml.dom.minidom import parseString
from django.core.management.base import NoArgsCommand
from study.models import *
from django.core import serializers
from django.template.base import NodeList

def input():
    parsingMaintag = 'perforList'
    parsingTitle = 'title'
    parsingSdate = 'startDate'
    parsingEdate = 'endDate'
    parsingArea = 'area'
    parsingRealmName = 'realmName'
    parsingPlace = 'place'
    parsingThumbnail = 'thumbnail'
    parsingGpsX = 'gpsX'
    parsingGpsY = 'gpsY'
    
    entry = xml_map.objects.all()
    url_m = 'http://www.culture.go.kr/openapi/rest/publicperformancedisplays/area?rows=1000&serviceKey=D1yyEu8AyO6FzCZ%2BaxokkVM8tpT6im7WFNB84Aewz9jXN5YkIA9txn1HRGx%2B3pZCidW3%2BNnRrbT1vc5QWFImxA%3D%3D' 
    mfile = urllib2.urlopen(url_m)
    mdata = mfile.read()
    mdom = parseString(mdata)
    mfile.close();
    for item in mdom.getElementsByTagName(parsingMaintag):        
        check = False;
        goalTitle=item.getElementsByTagName(parsingTitle)[0].firstChild.data
        for i in entry:
            if i.Title == goalTitle:
                check=True
                break
        if check == False:
            try:
                goalSdate=item.getElementsByTagName(parsingSdate)[0].firstChild.data
                goalEdate=item.getElementsByTagName(parsingEdate)[0].firstChild.data
                goalPlace=item.getElementsByTagName(parsingPlace)[0].firstChild.data
                goalArea=item.getElementsByTagName(parsingArea)[0].firstChild.data
                goalRealmName=item.getElementsByTagName(parsingRealmName)[0].firstChild.data
                goalThumbnil=item.getElementsByTagName(parsingThumbnail)[0].firstChild.data
                goalGpsX=item.getElementsByTagName(parsingGpsX)[0].firstChild.data
                goalGpsY=item.getElementsByTagName(parsingGpsY)[0].firstChild.data
                parsingSeq = item.getElementsByTagName('seq')[0].firstChild.data
                sdom = parseString(urllib2.urlopen('http://www.culture.go.kr/openapi/rest/publicperformancedisplays/d/?seq='+parsingSeq+'&serviceKey=r4kz8tI1CNlZ%2FCnyNqeS%2FqjFaWpwFfjbj%2BDlBFL7t5%2FaYDO5N63Ec748ICA0FQJ2dAzgWtY49qqNrgNF%2Bdvubw%3D%3D').read())
                goalContent = sdom.getElementsByTagName('contents1')[0].firstChild.data
                new_entry = xml_map(Title=goalTitle,Sdate=goalSdate,Edate=goalEdate,Content=goalContent,Addr_X=goalGpsX,Addr_Y=goalGpsY,mArea=goalArea,realmName=goalRealmName,mPlace=goalPlace,mThumbnil=goalThumbnil);        
                new_entry.save()
                print("Success!!!")
            except:
               print('Error..or not enough information'+goalTitle)          
        else:
            print("already exist"+goalTitle)
            
    q = xml_map.objects.all()
    for i in q:
        print i.Title
    print("end")
class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        input()

        
