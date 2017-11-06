from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):
    def setUp(self):
         self.obj = Subscription(
            name='Ana Claudia Nogueira',
            cpf='12345678901',
            email='anacnogueira@gmail.com',
            phone='12-998269414'
         )
         self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an aout created_at attribute."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Ana Claudia Nogueira', str(self.obj))




