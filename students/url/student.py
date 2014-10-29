__author__ = 'Iurii Sergiichuk'
from students.views import StudentCreateView, StudentDetailView, StudentUpdateView, StudentDeleteView

from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url('^new/$', StudentCreateView.as_view(), name="create_student"),
                       url('^(P<student_card_id>\w+)/$', StudentDetailView.as_view(), name="student_detail"),
                       url('^update/(P<student_card_id>\w+)/$', StudentUpdateView.as_view(), name="update_student"),
                       url('^delete/(P<student_card_id>\w+)/$', StudentDeleteView.as_view(), name="delete_student"),
)
