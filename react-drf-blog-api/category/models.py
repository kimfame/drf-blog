from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify

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
