from django.test import TestCase,Client
from django.contrib.auth.models import User
from django.urls import reverse
import json

class TestCase(TestCase):
    """docstring forTestCase."""
    print(reverse('index'))
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.history_url = reverse('profile')
        # User.objects.create_user('homer', 'ho...@simpson.net', 'simpson')
        # creates a user with username=homer and password=simpson
        user = User.objects.create_user('homer')
        user.set_password('simpson')
        user.save()

    def test_index_login(self):
        # checks if user login validation is working correctly
        response = self.client.get(self.index_url)
        self.assertTrue(self.client.login(username='homer',password='simpson'))
        self.assertEquals(response.status_code, 200)
        print("User login test successfull.")
        #wrong username check
        self.assertFalse(self.client.login(username='home',password='simpson'))


    def test_index_logout(self):
        # checks userlogout
        # logs in user first
        response = self.client.get(self.index_url)
        self.assertTrue(self.client.login(username='homer',password='simpson'))
        self.assertEquals(response.status_code, 200)
        # logsout user
        self.client.logout()
        self.assertEquals(response.status_code, 200)



    def test_index_GET(self):
        # checks if the homepage(index.html) template is working correctly
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'user/index.html')

    def test_profile_history(self):
        # checks if fine history is viewed correctly
        if(self.client.login(username='homer',password='simpson')):

            response = self.client.get(self.history_url)
            self.assertEquals(response.status_code,200)
            self.assertTemplateUsed(response,'user/profile.html')
