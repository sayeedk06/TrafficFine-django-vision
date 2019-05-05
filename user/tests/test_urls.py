from django.test import SimpleTestCase
from django.urls import reverse, resolve
from user.views import index,user_logout,profile

class TestUrls(SimpleTestCase):
    """checks to see if the functions in user.views.py uses the correct url """
    def test_index_url_resolved(self):
        url = reverse('index')
        # print(url)
        self.assertEquals(resolve(url).func,index)

    def test_logout_url_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func,user_logout)

    def test_profile_url_resolved(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func,profile)
