__author__ = 'Iurii Sergiichuk'
from django.conf.urls import patterns, url

from students.views import StudentCreateView, StudentDetailView, StudentUpdateView, StudentDeleteView

urlpatterns = patterns('',
                       url('^new/$', StudentCreateView.as_view(), name="create_student"),
                       url('^(?P<student_card_id>[0-9a-fA-F]{32})/$', StudentDetailView.as_view(),
                           name="student_detail"),
                       url('^update/(?P<student_card_id>[0-9a-fA-F]{32})/$', StudentUpdateView.as_view(),
                           name="update_student"),
                       url('^delete/(?P<student_card_id>[0-9a-fA-F]{32})/$', StudentDeleteView.as_view(),
                           name="delete_student"),
)
