# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url

from .views import (
    irc,
    QuienesSomos,
    MiembrosDePyAr,
    ListaDeCorreo
)

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', include('community.urls')),
    url(r'^irc/', irc, name='irc'),
    url(r'^aboutpyar/', QuienesSomos, name='about_pyar'),
    url(r'^members/', MiembrosDePyAr, name='pyar_members'),
    url(r'^maillinglist/', ListaDeCorreo, name='mailling_list'),
    url(r'^news/', include('news.urls')),
    url(r'^companies/', include('pycompanies.urls', namespace='companies')),
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^jobs/', include('jobs.urls')),
    url(r'^newbie/', include('newbie.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^events/', include('events.urls', namespace='events')),
    url(r'^faq/', include('faq.urls')),
    url(r'^planet/', include('planet.urls')),
    url(r'^wiki/', include('waliki.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
