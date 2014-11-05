from django.contrib.auth.views import login, logout

__author__ = 'Iurii Sergiichuk <i.sergiichuk@samsung.com>'

from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url('^login/$', login, kwargs={'template_name': 'students/auth/login.html',
                                                      'extra_context': {'action': '/students/auth/login/',
                                                                        'title': 'login'}},
                           name="login"),
                       url('^logout/$', logout, kwargs={'next_page': '/'},
                           name="logout"),
)