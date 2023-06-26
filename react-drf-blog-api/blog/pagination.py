from django.conf import settings
from rest_framework.pagination import PageNumberPagination


class PostPagination(PageNumberPagination):
    page_size = settings.POST_PAGE_SIZE

    def get_next_link(self):
        if not self.page.has_next():
            return None
        return self.page.next_page_number()

    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        return self.page.previous_page_number()
