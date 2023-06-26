from django.db.models import Subquery
from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from blog.models import Category, Post, Tag
from blog.pagination import PostPagination
from blog.serializers import (
    CategorySerializer,
    PostListSerializer,
    PostRetrieveSerializer,
    TagSerializer,
)
from core.utils import convert_str_list_to_int


class CategoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer


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


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostListSerializer
    pagination_class = PostPagination
    lookup_field = "slug"

    def get_queryset(self):
        post_filter_kwargs = {}

        for field_name in ["categories", "tags"]:
            query_param = self.request.query_params.get(field_name)
            id_list = (
                convert_str_list_to_int(query_param.split(",")) if query_param else None
            )
            if id_list:
                post_filter_kwargs[f"{field_name}__id__in"] = id_list

        posts = Post.public

        if len(post_filter_kwargs) > 0:
            posts = posts.filter(**post_filter_kwargs).distinct()
        else:
            posts = posts.all()

        posts = posts.order_by("-created_at")
        return posts

    def retrieve(self, request, slug=None):
        post = get_object_or_404(
            Post.public.select_related("author"),
            slug=slug,
        )
        post.hits += 1
        post.save(update_fields=["hits", "updated_at"])
        serializer = PostRetrieveSerializer(post, context={"request": request})
        return Response(serializer.data)
