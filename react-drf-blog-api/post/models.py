from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

from category.models import Category
from core.utils import add_random_suffix
from tag.models import Tag


class PublicPostManager(models.Manager):
    def filter(self, *args, **kwargs):
        if kwargs.get("is_published") == False:
            return super().get_queryset().filter(*args, **kwargs)
        return self.get_queryset().filter(*args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class Post(models.Model):
    slug = models.SlugField(max_length=300, unique=True, blank=True, allow_unicode=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=300)
    content = RichTextUploadingField()
    is_published = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    hits = models.BigIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    public = PublicPostManager()

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.previous_title = self.title

    def clean(self):
        slug_max_length = self._meta.get_field("slug").max_length

        remaining_slug_len = (
            slug_max_length - len(self.slug) - settings.POST_SLUG_SUFFIX_LEN
        )
        if remaining_slug_len < 0:
            raise ValidationError("title is too long to make a slug string.")

    def save(self, *args, **kwargs):
        if self.title != self.previous_title or self._state.adding:
            self.slug = slugify(value=self.title, allow_unicode=True)
            self.full_clean()
            self.slug = add_random_suffix(self.slug, settings.POST_SLUG_SUFFIX_LEN)
        super(Post, self).save(*args, **kwargs)

    def summary(self):
        return f"{self.content[:300]} ..."

    def __str__(self):
        return self.title
