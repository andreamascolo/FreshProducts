from django.urls import path
from django.contrib import admin

from . import views
#from django.conf.urls import url
'''
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
'''
urlpatterns = [
    path('home/', views.index, name='index'),
    path('home/login/', views.login, name='login'),
    path('home/contact/', views.contact, name='contact'),
    path('home/registrer/', views.registrer, name='registrer'),
    path('area_riservata/', views.area_riservata, name='area_riservata'),
    path('admin/', admin.site.urls),


    #url(r'^connection/','formView', name = 'loginform'),
    #url(r'^login/', 'login', name = 'login'),
]





