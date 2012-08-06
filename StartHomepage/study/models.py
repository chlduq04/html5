from django.db import models
from test.test_imageop import MAX_LEN

class categorie(models.Model):
    Title = models.CharField(max_length=40, null=False)
    class Admin:
        pass  
    def __unicode__(self):
        return self.Title

class directx_post(models.Model):
    Title = models.CharField(max_length=80, null=False)
    Content = models.TextField(max_length=1000, null=False)
    Created = models.DateTimeField(auto_now=True)
    Category = models.ForeignKey(categorie)
    class Admin:
        pass
    def __unicode__(self):
        return self.Title

class directx_comment(models.Model):
    post = models.ForeignKey(directx_post)
    Name = models.CharField(max_length=30)
    Content = models.TextField(max_length=500)
    def __unicode__(self):
        return self.Name
    

class django_post(models.Model):
    Title = models.CharField(max_length=80, null=False)
    Content = models.TextField(max_length=1000, null=False)
    Created = models.DateTimeField(auto_now=True)
    Category = models.ForeignKey(categorie)
    class Admin:
        pass
    def __unicode__(self):
        return self.Title

class django_comment(models.Model):
    post = models.ForeignKey(django_post)
    Name = models.CharField(max_length=30)
    Content = models.TextField(max_length=500)
    def __unicode__(self):
        return self.Name

class html_post(models.Model):
    Title = models.CharField(max_length=80, null=False)
    Content = models.TextField(max_length=1000, null=False)
    Created = models.DateTimeField(auto_now=True)
    Category = models.ForeignKey(categorie)
    class Admin:
        pass
    def __unicode__(self):
        return self.Title

class html_comment(models.Model):
    post = models.ForeignKey(html_post)
    Name = models.CharField(max_length=30)
    Content = models.TextField(max_length=500)
    def __unicode__(self):
        return self.Name

class opengl_post(models.Model):
    Title = models.CharField(max_length=80, null=False)
    Content = models.TextField(max_length=1000, null=False)
    Created = models.DateTimeField(auto_now=True)
    Category = models.ForeignKey(categorie)
    class Admin:
        pass
    def __unicode__(self):
        return self.Title

class opengl_comment(models.Model):
    post = models.ForeignKey(opengl_post)
    Name = models.CharField(max_length=30)
    Content = models.TextField(max_length=500)   
    def __unicode__(self):
        return self.Name

class ex_post(models.Model):
    Title = models.CharField(max_length=80, null=False)
    Content = models.TextField(max_length=1000, null=False)
    Created = models.DateTimeField(auto_now=True)
    Category = models.ForeignKey(categorie)
    class Admin:
        pass
    def __unicode__(self):
        return self.Title

class goo_map(models.Model):
    Title = models.CharField(max_length = 80,null=False,unique=True)
    Content = models.TextField(max_length = 1000,null=False)
    Addr_X = models.CharField(max_length=15,null=False)
    Addr_Y = models.CharField(max_length=15,null=False)
    mAddr = models.CharField(max_length=20,null=True)
    class Admin:
        pass
    def __unicode__(self):
        return self.Title

class xml_map(models.Model):
    Title = models.CharField(max_length = 80,null=False,unique=True)
    Sdate = models.CharField(max_length = 10)
    Edate = models.CharField(max_length = 10)
    Content = models.TextField(max_length = 1000,null=False)
    Addr_X = models.CharField(max_length=15,null=False)
    Addr_Y = models.CharField(max_length=15,null=False)
    realmName = models.CharField(max_length=10)
    mPlace = models.CharField(max_length=20)
    mArea = models.CharField(max_length=10)
    mThumbnil = models.CharField(max_length=30)
    class Admin:
        pass
    def __unicode__(self):
        return self.Title
class m_app(models.Model):
    Title = models.CharField(max_length=20)
    Location = models.CharField(max_length=30)
    Addr_X = models.CharField(max_length=12)
    Addr_Y = models.CharField(max_length=12)
    Comments = models.TextField(max_length=500)
    class Admin:
        pass
    def __unicode__(self):
        return self.Location

class upload_photo(models.Model):
    Title = models.ForeignKey(m_app)
    photo = models.FileField(upload_to='photos')
    class Admin:
        pass
    def __unicode__(self):
        return self.Location