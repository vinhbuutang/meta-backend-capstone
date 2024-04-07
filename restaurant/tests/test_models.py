from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=4.9, inventory=15)
        self.assertEqual(item.title, "IceCream")
        self.assertEqual(float(item.price), 4.9)
        self.assertEqual(str(item), "IceCream - 4.9")
