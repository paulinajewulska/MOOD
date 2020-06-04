from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import SignUp

class Test_urls(SimpleTestCase):

       def test_signup_url_is_resolved(self):
            url = reverse('signup')
            self.assertEquals(resolve(url).func.view_class, SignUp)
