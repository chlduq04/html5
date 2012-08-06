from study.models import *
from django.contrib import admin

class categories_admin(admin.ModelAdmin):
    display = ('Title')
class entries_admin(admin.ModelAdmin):
    list_display=('Title','Created','Category')    
class mapp_admin(admin.ModelAdmin):
    list_display=('Title','Addr_X','Addr_Y')
    
admin.site.register(categorie,categories_admin)    

admin.site.register(directx_post,entries_admin)    
admin.site.register(directx_comment)    

admin.site.register(opengl_post,entries_admin)    
admin.site.register(opengl_comment)    

admin.site.register(html_post,entries_admin)    
admin.site.register(html_comment)    

admin.site.register(django_post,entries_admin)    
admin.site.register(django_comment)    

admin.site.register(ex_post)

admin.site.register(goo_map)
admin.site.register(xml_map)
admin.site.register(m_app,mapp_admin)
admin.site.register(upload_photo)