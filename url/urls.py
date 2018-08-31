from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$', views.index, name='home'),
               url(r'^(\w{6})$', views.redirect_original, name='redirectoriginal'),
               url(r'^makeshort/$', views.shorten_url, name='shortenurl'),
               ]