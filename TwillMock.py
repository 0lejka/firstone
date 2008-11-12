import twill
import twill.extensions.check_links
IP = '127.0.0.1'
PORT = 8000
SITE = 'http://%s:%s' % (IP, PORT)

class TwillMock(object):

   def setup(self):
       '''
       - setup twill virtual web server
       '''
       from django.core.servers.basehttp import AdminMediaHandler
       from django.core.handlers.wsgi import WSGIHandler

       app = AdminMediaHandler(WSGIHandler())
       twill.add_wsgi_intercept(IP, PORT, lambda: app)
      
class TestLogin(TwillMock):

    def test_start_page(self):
        """
        Test start_page view
        """
        twill.commands.go(SITE)
        twill.commands.code(200)
        #twill.extensions.check_links.check_links(SITE)
    twill.extensions.check_links.check_links("127.0.0.1:8000")

    def test_login(self):
        twill.commands.go(SITE + '/accounts/login/')
        twill.commands.code(200)
        twill.commands.show()
        twill.commands.formvalue(1, 'username',  'test1')
        twill.commands.formvalue(1, 'password', 'test1')
        twill.commands.submit()
        twill.commands.code(200)


if __name__=="__main__":
    a=TestLogin()
    a.setup()
    a.test_start_page()
    a.test_login()
