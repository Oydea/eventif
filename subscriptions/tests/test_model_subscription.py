from django.test import TestCase
from datetime import datetime
from subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Luiz Silva',
            cpf='12345678901',
            email='foxyoxy87@gmail.com',
            phone='53-12345-6789'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Luiz Silva', str(self.obj))

    def test_paid_default_False(self):
        self.assertEqual(False, self.obj.paid)