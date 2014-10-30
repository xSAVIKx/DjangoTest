from django.conf.urls import patterns, include, url
from django.contrib import admin

from students.views import IndexView


urlpatterns = patterns('',
                       url(r'^$', IndexView.as_view(), name='index'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^students/', include('students.urls')),
)