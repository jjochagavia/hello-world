##from django.urls import path
#from django.conf.urls import include, path
#
#from . import views
#
#urlpatterns = [
#    path('', views.index, name='index'),
#]

from django.conf.urls import url
from django.conf.urls import include

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
]