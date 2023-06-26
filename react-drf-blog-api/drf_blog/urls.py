from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from category.views import CategoryViewSet
from tag.views import TagViewSet
from post.views import PostViewSet


router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="category")
router.register("tags", TagViewSet, basename="tag")
router.register("posts", PostViewSet, basename="post")

urlpatterns = router.urls

urlpatterns += [
    path(settings.ADMIN_URL, admin.site.urls),
    path("ckeditor/", include("ckeditor_uploader.urls")),
]

urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
