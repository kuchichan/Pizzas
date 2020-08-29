from django.test import TestCase
from django.core.exceptions import ValidationError
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from model_mommy import mommy
from polls.models import Pizza, Polling


class TestPizzasView(APITestCase):
    def setUp(self):
        self.uri = reverse("pizzas-list")
        mommy.make(Pizza)

    def test_register(self):
        pizza = Pizza.objects.all().last()
        current_votes = pizza.votes
        uri = f"{self.uri}{pizza.id}/vote/"

        response = self.client.patch(uri, data={})
        pizza.refresh_from_db()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(current_votes + 1, pizza.votes)

class TestPizzaModel(TestCase):

    def test_duplicate_pizzas_are_invalid_within_one_polling(self):
        same_topping = "Pineapple & Ham"
        polling = Polling.objects.create()
        Pizza.objects.create(polling=polling, topping=same_topping)
        with self.assertRaises(ValidationError):
            pizza = Pizza(polling=polling, topping=same_topping)
            pizza.full_clean()
        
