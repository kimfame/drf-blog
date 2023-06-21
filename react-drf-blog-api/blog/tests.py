import random

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import CategoryFactory, PostFactory, TagFactory
from .models import Post


class CategoryTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("category-list")
        CategoryFactory.create_batch(size=10)

    def test_can_get_all_categories(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)


class TagTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("tag-list")
        TagFactory.create_batch(size=10)

    def test_can_get_all_tags(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)


class PostTestCase(APITestCase):
    def test_can_get_only_posts_published(self):
        PostFactory.create_batch(size=random.randint(10, 20))
        post_count = Post.objects.filter(is_published=True).count()
        url = reverse("post-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(dict(response.data.items())["count"], post_count)

    def test_can_filter_categories(self):
        categories = CategoryFactory.create_batch(size=random.randint(5, 10))

        for _ in range(30):
            PostFactory.create(
                categories=random.choices(categories, k=random.randint(1, 3))
            )

        target_category_id_list = [
            c.id for c in random.choices(categories, k=random.randint(1, 5))
        ]

        post_count = (
            Post.objects.filter(
                categories__id__in=target_category_id_list,
                is_published=True,
            )
            .distinct()
            .count()
        )
        base_url = reverse("post-list")
        query_string = f"categories={','.join(map(str, target_category_id_list))}"
        url = f"{base_url}?{query_string}"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(dict(response.data.items())["count"], post_count)

    def test_can_filter_tags(self):
        tags = TagFactory.create_batch(size=random.randint(10, 20))

        for _ in range(30):
            PostFactory.create(tags=random.choices(tags, k=random.randint(3, 5)))

        target_tags_id_list = [
            t.id for t in random.choices(tags, k=random.randint(1, 5))
        ]

        post_count = (
            Post.objects.filter(tags__id__in=target_tags_id_list, is_published=True)
            .distinct()
            .count()
        )

        base_url = reverse("post-list")
        query_string = f"tags={','.join(map(str, target_tags_id_list))}"
        url = f"{base_url}?{query_string}"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(dict(response.data.items())["count"], post_count)

    def test_can_filter_categories_and_tags(self):
        categories = CategoryFactory.create_batch(size=5)
        tags = TagFactory.create_batch(size=10)

        for _ in range(20):
            PostFactory.create(
                categories=random.choices(categories, k=random.randint(1, 3)),
                tags=random.choices(tags, k=random.randint(3, 5)),
            )

        target_category = random.choice(categories).id
        target_tag = random.choice(tags).id

        post_count = Post.objects.filter(
            categories__id=target_category,
            tags__id=target_tag,
            is_published=True,
        ).count()

        base_url = reverse("post-list")
        query_string = f"categories={target_category}&tags={target_tag}"
        url = f"{base_url}?{query_string}"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(dict(response.data.items())["count"], post_count)
