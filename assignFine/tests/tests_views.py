from django.test import TestCase,Client
from django.contrib.auth.models import User
from assignFine.models import Fine
from assignFine.forms import FineForm
from django.urls import reverse
import json

class TestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # gets url for assigning fine function
        self.fine_url = reverse('assignFine')
        # creates a user with username darth_vader and password father
        user = User.objects.create_user('darth_vader')
        user.set_password('father')
        user.save()


    def test_fine_form(self):
        if(self.client.login(username='darth_vader',password='father')):
# checks if amount field in form takes positive values
            form = FineForm(data={'amount': 200})
            self.assertTrue(form.is_valid())
# checks if amount field in form gives an error for negative amount
            form = FineForm(data={'amount': -200})
            self.assertFalse(form.is_valid())
# checks if amount field in form gives an error for string value
            form = FineForm(data={'amount': 'asdasd'})
            self.assertFalse(form.is_valid())
# checks if amount field in form works for string number value
            form = FineForm(data={'amount': "125"})
            self.assertTrue(form.is_valid())
# checks if amount field in form works for string number value
            form = FineForm(data={'amount': "-125"})
            self.assertFalse(form.is_valid())
