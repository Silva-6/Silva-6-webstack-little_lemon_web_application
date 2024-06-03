from django.tests import Testcase
from restaurant.models import Menu

class MenuViewTest(TestCase):

    def setup(self):
        self.items = [
            Menu.objects.create(title="IceCream", price=80, inventory=100),
            Menu.objects.create(title="Burgars", price=90, inventory=120),
            Menu.objects.create(title="Grocerries", price=180, inventory=20),
            Menu.objects.create(title="Balloons", price=70, inventory=100)
        ]
        
    def test_getall(self):
        for item in self.items:
            self.assertEqual(item, f"{item.title} : {item.price}")
