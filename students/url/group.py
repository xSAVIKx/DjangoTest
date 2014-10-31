__author__ = 'Iurii Sergiichuk'
from django.conf.urls import patterns, url

from students.views import GroupCreateView, GroupDetailView, GroupUpdateView, GroupDeleteView

urlpatterns = patterns('',
                       url('^new/$', GroupCreateView.as_view(), name="create_group"),
                       url('^(?P<group_id>\d+)/$', GroupDetailView.as_view(), name="group_detail"),
                       url('^edit/(?P<group_id>\d+)/$', GroupUpdateView.as_view(), name="edit_group"),
                       url('^delete/(?P<group_id>\d+)/$', GroupDeleteView.as_view(), name="delete_group"),
)
