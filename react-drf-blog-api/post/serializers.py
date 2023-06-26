from rest_framework import serializers

from core import utils
from .models import Post


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    slug = serializers.CharField(read_only=True)


class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    slug = serializers.CharField(read_only=True)


class PostListSerializer(serializers.Serializer):
    slug = serializers.SlugField()
    title = serializers.CharField()
    summary = serializers.SerializerMethodField()
    categories = CategorySerializer(many=True, read_only=True)
    created_at = serializers.CharField()

    def get_summary(self, obj):
        return utils.remove_tags(obj.summary())

    class Meta:
        model = Post
        fields = [
            "slug",
            "title",
            "summary",
            "categories",
            "created_at",
        ]


class PostRetrieveSerializer(serializers.ModelSerializer):
    next = serializers.SerializerMethodField()
    previous = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    tags = TagSerializer(many=True, read_only=True)

    def get_next(self, obj):
        post = (
            Post.public.filter(
                pk__gt=obj.pk,
            )
            .order_by("pk")
            .first()
        )
        if post:
            return {"slug": post.slug, "title": post.title}
        else:
            return None

    def get_previous(self, obj):
        post = (
            Post.public.filter(
                pk__lt=obj.pk,
            )
            .order_by("-pk")
            .first()
        )
        if post:
            return {"slug": post.slug, "title": post.title}
        else:
            return None

    def get_author(self, obj):
        return obj.author.username

    class Meta:
        model = Post
        fields = [
            "next",
            "previous",
            "slug",
            "title",
            "author",
            "content",
            "tags",
            "created_at",
        ]
