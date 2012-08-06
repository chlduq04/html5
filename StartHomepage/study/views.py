# -*- coding: utf-8 -*-
import urllib, json, requests,sys,urllib2
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, loader
from study.models import *
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django import forms
from django.views.decorators.csrf import csrf_exempt
from xml.dom import minidom
from django.utils import simplejson
from django.core.context_processors import request
from base64 import decode
from django.core import serializers
from django.shortcuts import render_to_response
from cgi import log
#def Post_list(request):
#    return render_to_response('post_list.html', {'posts' : Post.objects.order_by('-Created')[:5],})

#def Post_detail(request, post_id):
#    post = Post.objects.get(id=post_id)
#    return render_to_response('post_detail.html', {
#        'post' : post,
#        'comments' : post.Comment.all(),
#        'comment_add_form' : forms.FormWrapper(Comment.AddManipulator(), {}, {}),
#        })

#def Add_comment(request, post_id):
#    manipulator = Comment.AddManipulator()
#    comment_data = request.POST.copy()
#    comment_data['post'] = post_id
#    manipulator.do_html2python(comment_data)
#    manipulator.save(comment_data)
#    return HttpResponseRedirect("../")
#장



def mainframe(request):
    tpl = loader.get_template('MainFrame.html')
    ctx = Context({})
    return HttpResponse(tpl.render(ctx))

def openglpage(request):
    tpl = loader.get_template('OpenglPage.html')
    ctx = Context({})
    return HttpResponse(tpl.render(ctx))

def openglpagelist(request,page=1):
    page = int(page)
    per_page = 5
    start_pos = (page - 1) * 5
    end_pos = start_pos + 5
    categories = categorie.objects.all()
    entries = opengl_post.objects.all().order_by('-Created')[start_pos:end_pos]
    page_num = opengl_post.objects.count() / per_page + 1
    tpl = loader.get_template('Opengllist.html')
    ctx = Context({
                   'entries':entries,
                   'pagenum':page_num,
                   'categories':categories
                   })
    return HttpResponse(tpl.render(ctx))


@csrf_exempt    
def openglpost(request):
    if request.POST.has_key('name_field')==False:
        return HttpResponse('한글자라도 입력하세요')
    else:
        if len(request.POST['name_field']) ==0:
            return HttpResponse('한글자라도 넣어요')
        else:    
            entry_title = request.POST['name_field']
            entry_content = request.POST['content_field']
            entry_category = categorie.objects.get(id=request.POST['category_field'])
            new_entry = opengl_post(Title=entry_title, Content=entry_content, Category=entry_category)
            try:
                new_entry.save()
                return HttpResponse('Success!!!')              
            except:
                return HttpResponse('Error..')

def map(request):
    if request.is_ajax():
        data = serializers.serialize("json", goo_map.objects.all())
        return HttpResponse(data,mimetype='text/plain')
    else:
        data = goo_map.objects.all()
#        tpl = loader.get_template('googlemap.html')
#        return HttpResponse(tpl.render(Context({'data':data})))
        return render_to_response("googlemap.html",{"data":data})
    

#def map(requset):
#    entry = goo_map.objects.all()
#    lat=[]
#    for i in entry:
#        lat.append((i.Title.replace('\r\n', ''),i.Content.replace('\r\n', ''),i.Addr_X.Content.replace('\r\n', ''),i.Addr_Y.Content.replace('\r\n', ''),i.mAddr.replace('\r\n', '')))
#    tpl = loader.get_template('exgooglemap.html')
#    ctx = Context({
#                   'prs_detail': lat
#                   })
#    return HttpResponse(tpl.render(ctx))

def exmap(requset):
    tpl = loader.get_template('exgooglemap.html')
#    url_c = u"http://openapi.seoul.go.kr:8088/json/4150495f3230383363686c6475713034/%EB%AC%B8%ED%99%94%EC%8B%9C%EC%84%A4%20%EC%83%81%EC%84%B8%20%EC%A0%95%EB%B3%B4%20%EC%A0%9C%EA%B3%B5/1/10/100562/" 
#    rc = json.loads(requests.get(url_c).content.decode("utf-8"))
#    lat_c = []
#    for i,k in rc.iteritems():
#        for l,m in k.iteritems():
#            lat_c.append((m[u'FAC_NAME'] ,m[u'MAIN_IMG'],m[u'ENTR_FEE']))

    url_m = u"http://openapi.seoul.go.kr:8088/json/4150495f3230383363686c6475713034/%EC%A0%84%ED%86%B5%EC%8B%9C%EC%9E%A5%20%EC%A0%95%EB%B3%B4/1/50/" 
    rm = json.loads(requests.get(url_m).content.decode("utf-8"))
        
    lat_m = []    
    
    for i,k in rm.iteritems():
        for l,m in k.iteritems():
            lat_m.append((str(m[u'M_SUBWAY']).encode('utf-8').replace('\r\n', ''), str(m[u'M_NAME']).encode('utf-8').replace('\r\n', ''),str(m[u'M_PARKING']).encode('utf-8').replace('\r\n', ''),str(m[u'M_ADDR']).encode('utf-8').replace('\r\n', '')))
    ctx = Context({
                   'prs_detail': lat_m
                   })
    
    return HttpResponse(tpl.render(ctx))


def mobile_json_marketinfo(request):
    data = serializers.serialize("json", goo_map.objects.all())
    return HttpResponse(data,mimetype='text/plain')
def mobile_xmlmap(request):
    data = serializers.serialize("json", xml_map.objects.all())
    return HttpResponse(data,mimetype='text/plain')

@csrf_exempt 
def input_db(request):
    printm="Fail"
    entry_location = request.POST.get('Location')
    if entry_location:
        
        setDB = myapp(Location=entry_location)
        try:
            setDB.save()
            printm = "Success!"
        except:
            printm = "Error!!"
    
    return HttpResponse(printm)

@csrf_exempt 
def search_loc(request):
    printm="Fail"
    entry_title = request.POST.get('Title')
    entry_location = request.POST.get('Location')
    entry_loc_encode = request.POST.get('Loc_encode')
    entry_comment = request.POST.get('Comment')
    if entry_location and entry_title:
        try:
            go_url = urllib2.urlopen('http://maps.googleapis.com/maps/api/geocode/json?sensor=false&language=ko&address=%s' % entry_loc_encode)
            road_map = json.loads(go_url.read(),encoding='utf-8')
            setDB = m_app(Title = entry_title,Location = entry_location,Addr_X=road_map['results'][0]['geometry']['location']['lat'],Addr_Y=road_map['results'][0]['geometry']['location']['lng'],Comments = entry_comment)
            setDB.save()
            printm = "Success"
        except:
            printm = "Error!!"+entry_location
    return HttpResponse(printm)

def mobile_loc(request):
    data = serializers.serialize("json", m_app.objects.all())
    return HttpResponse(data,mimetype='text/plain')