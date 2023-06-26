from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import CategoryFactory


class CategoryTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("category-list")
        CategoryFactory.create_batch(size=10)

    def test_can_get_all_categories(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)
