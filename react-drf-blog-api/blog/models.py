from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

from core.utils import add_random_suffix


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(
        max_length=30,
        unique=True,
        blank=True,
        allow_unicode=True,
        editable=False,
    )

    def clean(self):
        slug_max_length = self._meta.get_field("slug").max_length

        remaining_slug_len = (
            slug_max_length - len(self.slug) - settings.CATEGORY_SLUG_SUFFIX_LEN
        )
        if remaining_slug_len < 0:
            raise ValidationError("name is too long to make a slug string.")

    def save(self, *args, **kwargs):
        self.slug = slugify(value=self.name, allow_unicode=True)
        self.full_clean()
        self.slug = add_random_suffix(self.slug, settings.CATEGORY_SLUG_SUFFIX_LEN)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(
        max_length=50,
        unique=True,
        blank=True,
        allow_unicode=True,
        editable=False,
    )

    def clean(self):
        slug_max_length = self._meta.get_field("slug").max_length

        remaining_slug_len = (
            slug_max_length - len(self.slug) - settings.TAG_SLUG_SUFFIX_LEN
        )
        if remaining_slug_len < 0:
            raise ValidationError("name is too long to make a slug string.")

    def save(self, *args, **kwargs):
        self.slug = slugify(value=self.name, allow_unicode=True)
        self.full_clean()
        self.slug = add_random_suffix(self.slug, settings.TAG_SLUG_SUFFIX_LEN)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


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
