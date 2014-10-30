__author__ = 'Iurii Sergiichuk'

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^group/', include('students.url.group')),
                       url(r'^student/', include('students.url.student')),
)
