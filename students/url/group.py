from django.contrib.auth.decorators import login_required

__author__ = 'Iurii Sergiichuk'
from django.conf.urls import patterns, url

from students.views import GroupCreateView, GroupDetailView, GroupEditView, GroupDeleteView

urlpatterns = patterns('',
                       url('^new/$', login_required(GroupCreateView.as_view()), name="create_group"),
                       url('^(?P<group_id>\d+)/$', GroupDetailView.as_view(), name="group_detail"),
                       url('^edit/(?P<group_id>\d+)/$', login_required(GroupEditView.as_view()), name="edit_group"),
                       url('^delete/(?P<group_id>\d+)/$', login_required(GroupDeleteView.as_view()),
                           name="delete_group"),
)
