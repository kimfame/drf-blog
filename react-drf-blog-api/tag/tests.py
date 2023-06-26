import random

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from post.factories import PostFactory
from post.models import Post
from .factories import TagFactory


class TagTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("tag-list")

    def test_can_get_all_tags(self):
        tags = TagFactory.create_batch(size=10)

        for _ in range(30):
            PostFactory.create(
                tags=random.choices(tags, k=random.randint(1, 3)),
            )

        public_post_tag_count = Post.public.all().values("tags").distinct().count()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), public_post_tag_count)


class TagTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("tag-list")

    def test_can_get_all_tags(self):
        tags = TagFactory.create_batch(size=10)

        for _ in range(30):
            PostFactory.create(
                tags=random.choices(tags, k=random.randint(1, 3)),
            )

        public_post_tag_count = Post.public.all().values("tags").distinct().count()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), public_post_tag_count)
