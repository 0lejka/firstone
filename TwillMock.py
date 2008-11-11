 # -*- coding: utf-8 -*-
 IP = '127.0.0.1'
 PORT = 8080
 SITE = 'http://%s:%s' % (IP, PORT)

 class TwillMock(object):

    def setup(self):
        '''
        - setup twill virtual web server
        '''
        from django.core.servers.basehttp import AdminMediaHandler
        from django.core.handlers.wsgi import WSGIHandler

        app = AdminMediaHandler(WSGIHandler())
        add_wsgi_intercept(IP, PORT, lambda: app)
