from django.test import TestCase
from django.urls import reverse

# my tests

class LoginTestCase(TestCase):

    def test_login(self):
        login_url = 'login'
        url2 = 'mylogin'
        data = {'username': 'john', 'password': '124'}
        self.response = self.client.post(reverse('login'))
        self.response = self.client.post(login_url, data)

        self.assertEqual(self.response.status_code, 200)
        print(self.response.status_code)
        self.assertTemplateUsed(self.response, 'base/login.htm')

class RegisterTestCase(TestCase):

    def test_register(self):
        self.response = self.client.post(reverse('register'))

        self.assertTemplateUsed(self.response, 'base/register.html')
        self.assertEqual(self.response.status_code, 200)

class HomeTestCase(TestCase):

    def test_home(self):
        self.response = self.client.post(reverse('home'))

        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'base/home.html')


class ActivityTestCase(TestCase):

    def test_activity(self):
        self.response = self.client.post(reverse('activity'))

        self.assertEqual(self.response.status_code, 200)
        self.asserTemplateUsed(self.response, 'base/activity.html')

class FooterTestCase(TestCase):

    def test_footer(self):
        self.response = self.client.post(reverse('footer_page'))

        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'base/footer_page.html')