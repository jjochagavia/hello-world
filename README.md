# hello-world

TUTORIAL DJANGO

Ojo con esto:
Now’s a good time to note: don’t use this server in anything resembling a production environment. 
It’s intended only for use while developing. (We’re in the business of making Web frameworks, not Web servers.)

Hay q reiniciar el servidor al agregar archivos

Siempre usar include en el mysite/urls, la excepcion es el del admin

MODIFICAR URLs según esto, no tutorial. Problema de versiones de django

in mysite/urls.py tener:

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
url(r'^polls/', include('polls.urls')),
url(r'^admin/', admin.site.urls),
]

y luego, según corresponda para la app:

app/urls.py tener:

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



