from django.test import TestCase
from fp_client import models

class UserTestCase(TestCase):
	def setUp(self):
		Users.objects.create(email="hi@mit.edu", password="asdf")
		Users.objects.create(email="bye@mit.edu", password="asdf")
