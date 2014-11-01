__author__ = 'iurii'

from django.conf import settings


def settings(request):
    return {'settings': settings}
