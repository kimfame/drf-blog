from factory import sequence
from factory.django import DjangoModelFactory

from .models import Tag


class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag

    name = sequence(lambda n: f"tag_{n+1}")
