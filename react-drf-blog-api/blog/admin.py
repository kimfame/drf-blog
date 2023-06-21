from django.contrib import admin
from django.contrib.auth.models import User

from blog.models import Category, Post, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("name",)
    exclude = ("slug",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("name",)
    exclude = ("slug",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "slug",
        "category_list",
        "tag_list",
        "hits",
        "is_published",
        "created_at",
    )
    list_display_links = ("title",)
    exclude = ("slug",)
    list_filter = ("tags__name",)
    search_fields = ("title", "content")

    def get_form(self, request, obj=None, **kwargs):
        form = super(PostAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields["author"].initial = User.objects.all().order_by("id").first()
        return form

    def category_list(self, obj):
        return ", ".join([c.name for c in obj.categories.all()])

    def tag_list(self, obj):
        return ", ".join([t.name for t in obj.tags.all()])
