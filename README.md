# hello-world

TUTORIAL DJANGO

Ojo con esto:
Now’s a good time to note: don’t use this server in anything resembling a production environment. 
It’s intended only for use while developing. (We’re in the business of making Web frameworks, not Web servers.)

Hay q reiniciar el servidor al agregar archivos

Siempre usar include en el mysite/urls, la excepcion es el del admin

MODIFICAR URLs según esto, no tutorial. Problema de versiones de django

in polls/urls.py

from django.conf.urls import url
from django.conf.urls import include

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
]

three-step guide to making model changes:

Change your models (in models.py).
Run python manage.py makemigrations to create migrations for those changes
Run python manage.py migrate to apply those changes to the database.



