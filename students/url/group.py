__author__ = 'Iurii Sergiichuk'
from students.views import GroupCreateView, GroupDetailView, GroupUpdateView, GroupDeleteView

from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url('^new/$', GroupCreateView.as_view(), name="create_group"),
                       url('^(P<group_title>\w+)/$', GroupDetailView.as_view(), name="group_detail"),
                       url('^update/(P<group_title>\w+)/$', GroupUpdateView.as_view(), name="update_group"),
                       url('^delete/(P<group_title>\w+)/$', GroupDeleteView.as_view(), name="delete_group"),
)
