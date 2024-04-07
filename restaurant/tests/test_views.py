from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.core.serializers import serialize


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        Menu.objects.create(title="IceCream", price=4.9, inventory=15)
        Menu.objects.create(title="Mango Salad", price=12.9, inventory=10)
        Menu.objects.create(title="Pho", price=15.9, inventory=20)

    def test_getall(self):
        # get the url for the view we are testing
        # assuming we named our URL 'menu-list'
        response = self.client.get(reverse('menu_list'))

        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, 200)
