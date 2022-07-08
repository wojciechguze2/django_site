import math


class Pagination:
    def __init__(self, queryset, request_page_number: int = 1, limit: int = 5):
        if isinstance(queryset, list):
            self.queryset_count = len(queryset)
        else:
            self.queryset_count = queryset.count()

        self.limit = limit
        self.pages_count = math.ceil(self.queryset_count / self.limit)
        self.page_number = self.get_page_number(request_page_number)
        self.offset = (self.page_number - 1) * self.limit

        if self.page_number == -1 and self.queryset_count % self.limit == 0:
            self.page_results = queryset[self.limit * -1:]
        elif self.page_number == -1 and self.queryset_count % self.limit != 0:
            self.page_results = queryset[(self.queryset_count % self.limit) * -1:]
        else:
            self.page_results = queryset[self.offset:self.offset + self.limit]

        self.current = self.page_number
        self.previous = self.current - 1 if self.current - 1 > 0 else None
        self.next = self.current + 1 if self.current < self.pages_count else None

    def get_json(self):
        if self.current == -1:  # last
            return {
                'previous': self.pages_count - 1,
                'current': self.pages_count,
                'next': None
            }
        else:
            return {
                'previous': self.previous,
                'current': self.current,
                'next': self.next
            }

    @staticmethod
    def get_page_number(request_page_number: int or None) -> int:
        if request_page_number and request_page_number == 'first':
            page_number = 1
        elif request_page_number and request_page_number == 'last':
            page_number = -1
        elif request_page_number:
            page_number = int(request_page_number)
        else:
            page_number = 1

        return page_number
