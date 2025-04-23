import collections

from django.core.paginator import EmptyPage, PageNotAnInteger
from django.utils.translation import gettext_lazy as _


class CountlessPage:
    def __init__(self, object_list, number, page_size):
        self.object_list = object_list
        self.number = number
        self.page_size = page_size
        self._has_next = len(self.object_list) > self.page_size
        self.object_list = self.object_list[:self.page_size]

    def __iter__(self):
        return iter(self.object_list)

    def has_next(self):
        return self._has_next

    def has_previous(self):
        return self.number > 1

    def has_other_pages(self):
        return self.has_previous() or self.has_next()

    def next_page_number(self):
        if not self.has_next():
            raise EmptyPage("No next page.")
        return self.number + 1

    def previous_page_number(self):
        if not self.has_previous():
            raise EmptyPage("No previous page.")
        return self.number - 1

    def start_index(self):
        return (self.number - 1) * self.page_size + 1

    def end_index(self):
        return self.start_index() + len(self.object_list) - 1

    def total_pages(self):
        if self.total_count is None:
            return None
        return (self.total_count + self.page_size - 1) // self.page_size


class CountlessPaginator:
    def __init__(self, object_list, per_page) -> None:
        self.object_list = object_list
        self.per_page = per_page

    def validate_number(self, number):
        try:
            if isinstance(number, float) and not number.is_integer():
                raise ValueError
            number = int(number)
        except (TypeError, ValueError):
            raise PageNotAnInteger(_("Page number is not an integer"))
        if number < 1:
            raise EmptyPage(_("Page number is less than 1"))
        return number

    def get_page(self, number):
        try:
            number = self.validate_number(number)
        except (PageNotAnInteger, EmptyPage):
            number = 1
        return self.page(number)

    def page(self, number):
        number = self.validate_number(number)
        bottom = (number - 1) * self.per_page
        top = bottom + self.per_page
        return CountlessPage(
            self.object_list[bottom:top + 1],  # fetch one extra to check has_next
            number,
            self.per_page
        )
