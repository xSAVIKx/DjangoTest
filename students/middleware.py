import datetime

from django.db import connection
from django.http.response import HttpResponse

HttpResponse

__author__ = 'iurii'


class DatabasePerformanceMiddleware(object):
    def __init__(self):
        self.start_time = None


    def process_request(self, request):
        self.start_time = datetime.datetime.utcnow()

    def process_response(self, request, response):
        if 'text/html' in response.get('content-type'):
            request_time = datetime.datetime.utcnow() - self.start_time
            sql_queries_amount = len(connection.queries)
            content = response.content
            content = content.replace('</body>', 'request_time=%s, sql_queries_amount=%s\n</body>' % (
                str(request_time), str(sql_queries_amount)))
            response.content = content
        return response