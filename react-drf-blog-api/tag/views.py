from django.db.models import Subquery
from rest_framework import mixins, viewsets

from core.utils import convert_str_list_to_int
from post.models import Post
from .models import Tag
from .serializers import TagSerializer


class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = TagSerializer

    def get_queryset(self):
        category_param = self.request.query_params.get("categories")

        if category_param:
            category_id_list = convert_str_list_to_int(category_param.split(","))

            return Tag.objects.filter(
                id__in=Subquery(
                    Post.public.filter(categories__id__in=category_id_list)
                    .prefetch_related("categories")
                    .values("tags")
                    .distinct()
                )
            ).order_by("name")

        return Tag.objects.filter(
            id__in=Subquery(Post.public.all().values("tags").distinct())
        ).order_by("name")
