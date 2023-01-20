from django.test import TestCase,SimpleTestCase,Client
from django.urls import reverse,resolve
from .views import Userviewlist
# Create your tests here.
class DemoTest(TestCase):
    def runTest(self):
        c= Client()
        username = input('enter username: ')
        url = '/user/api/user/'+username+'/'
        res = c.get(url)
        self.assertEqual(res.status_code,200)