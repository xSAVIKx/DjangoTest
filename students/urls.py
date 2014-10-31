from students.views import HomeRedirectView

__author__ = 'Iurii Sergiichuk'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', HomeRedirectView.as_view(), name='index_redirect'),
                       url(r'^group/', include('students.url.group')),
                       url(r'^student/', include('students.url.student')),
)
