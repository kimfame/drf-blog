import random

from django.contrib.auth.models import User
from factory import fuzzy, LazyAttribute, post_generation, sequence, SubFactory
from factory.django import DjangoModelFactory
from faker import Faker

from core.utils import random_html_paragraphs
from .models import Category, Post, Tag

fake = Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = sequence(lambda n: f"user_{n+1}")


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = sequence(lambda n: f"category_{n+1}")


class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag

    name = sequence(lambda n: f"tag_{n+1}")


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    author = SubFactory(UserFactory)
    title = sequence(lambda n: f"title_{n+1}")
    content = LazyAttribute(lambda _: random_html_paragraphs(1, 10))
    is_published = fuzzy.FuzzyChoice(choices=[True, False])

    @post_generation
    def categories(self, create, extracted, **kwargs):
        if extracted:
            for category in extracted:
                self.categories.add(category)

        if create and not extracted:
            self.categories.add(
                *CategoryFactory.create_batch(size=random.randint(1, 3))
            )

    @post_generation
    def tags(self, create, extracted, **kwargs):
        if extracted:
            for tag in extracted:
                self.tags.add(tag)

        if create and not extracted:
            self.tags.add(*TagFactory.create_batch(size=random.randint(1, 5)))
