__author__ = 'Iurii Sergiichuk'
from django.conf.urls import patterns, url

from students.views import StudentCreateView, StudentDetailView, StudentUpdateView, StudentDeleteView

urlpatterns = patterns('',
                       url('^new/$', StudentCreateView.as_view(), name="create_student"),
                       url('^(?P<student_id>\d+)/$', StudentDetailView.as_view(),
                           name="student_detail"),
                       url('^edit/(?P<student_id>\d+)/$', StudentUpdateView.as_view(),
                           name="edit_student"),
                       url('^delete/(?P<student_id>\d+)/$', StudentDeleteView.as_view(),
                           name="delete_student"),
)
