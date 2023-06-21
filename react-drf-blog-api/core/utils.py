from __future__ import annotations

import random
import re
import string

from secrets import choice

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from faker import Faker

fake = Faker()


def add_random_suffix(
    value: str,
    suffix_length: int,
):
    if not value:
        raise ValidationError("value must not be empty.", code="invalid")
    if suffix_length < 1:
        raise ValidationError(
            "suffix_length is greater than or equal to 1", code="min_value"
        )

    return f"{value}-{get_random_string(suffix_length)}"


def convert_str_list_to_int(str_list: list[str]) -> list[int]:
    return list(set(int(s) for s in str_list if s.isdigit() and int(s) > 0))


def get_random_string(length: int) -> str:
    return "".join(
        [choice(string.ascii_letters + string.digits) for _ in range(length)]
    )


def random_html_paragraphs(min=5, max=10):
    return "<br/>".join(
        [
            f"<p>{fake.paragraph(nb_sentences=random.randint(100, 300))}</p>"
            for _ in range(random.randint(min, max))
        ]
    )


def remove_tags(str: str):
    cleanr = re.compile("<.*?>")
    return re.sub(cleanr, "", str)
