from factory import sequence
from factory.django import DjangoModelFactory

from .models import Category


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = sequence(lambda n: f"category_{n+1}")
