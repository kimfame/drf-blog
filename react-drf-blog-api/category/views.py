from rest_framework import mixins, viewsets

from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
