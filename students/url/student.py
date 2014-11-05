from django.contrib.auth.decorators import login_required

__author__ = 'Iurii Sergiichuk'
from django.conf.urls import patterns, url

from students.views import StudentCreateView, StudentDetailView, StudentEditView, StudentDeleteView

urlpatterns = patterns('',
                       url('^new/$', login_required(StudentCreateView.as_view()), name="create_student"),
                       url('^(?P<student_id>\d+)/$', StudentDetailView.as_view(),
                           name="student_detail"),
                       url('^edit/(?P<student_id>\d+)/$', login_required(StudentEditView.as_view()),
                           name="edit_student"),
                       url('^delete/(?P<student_id>\d+)/$', login_required(StudentDeleteView.as_view()),
                           name="delete_student"),
)
