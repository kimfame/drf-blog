import logging
import random

from django.contrib.auth.models import User
from django.db import OperationalError
from faker import Faker

from category.factories import CategoryFactory
from post.factories import PostFactory, UserFactory
from tag.factories import TagFactory
from .test_data import category_list, tag_list

logger = logging.getLogger(__name__)
fake = Faker()


def run():
    create_superuser()
    categories = create_categories(category_list)
    tags = create_tags(tag_list)
    create_posts(categories, tags, 100)


def create_superuser():
    logger.info("Create a superuser...")
    try:
        if User.objects.filter(is_superuser=True).exists():
            logger.info("Superuser already exists.")
        else:
            User.objects.create_superuser(
                "admin@test.com", "admin@test.com", "admin@test.com"
            )
            logger.info("Superuser created successfully.")
    except OperationalError as e:
        logger.error(e, exc_info=True)


def create_categories(category_name_list=None):
    logger.info("Create categories...")
    if category_name_list:
        category_obj_list = []
        for name in category_name_list:
            category_obj_list.append(CategoryFactory.create(name=name))
        return category_obj_list
    else:
        return CategoryFactory.create_batch(size=15)


def create_tags(tag_name_list=None):
    logger.info("Create tags...")
    if tag_name_list:
        tag_obj_list = []
        for name in tag_name_list:
            tag_obj_list.append(TagFactory.create(name=name))
        return tag_obj_list
    else:
        return TagFactory.create_batch(size=30)


def create_posts(categories=None, tags=None, num=100):
    logger.info("Create posts...")
    user = UserFactory.create()

    if categories and tags and num > 0:
        for _ in range(num):
            PostFactory.create(
                title=fake.paragraph(nb_sentences=1, variable_nb_sentences=False),
                author=user,
                categories=random.choices(categories, k=random.randint(1, 3)),
                tags=random.choices(tags, k=random.randint(1, 5)),
            )
