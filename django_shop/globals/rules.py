class Pagination:
    def __init__(self, queryset, page_number: int = 1, limit: int = 5):
        if isinstance(queryset, list):
            self.queryset_count = len(queryset)
        else:
            self.queryset_count = queryset.count()

        self.limit = limit
        self.pages_count = self.queryset_count / self.limit
        self.page_number = page_number
        self.offset = (self.page_number - 1) * self.limit
        self.page_results = queryset[self.offset:self.offset + self.limit]

        self.current = self.page_number
        self.previous = self.current - 1 if self.current - 1 > 0 else None
        self.next = self.current + 1 if self.current < self.pages_count else None

    def get_json(self):
        return {
            'previous': self.previous,
            'current': self.current,
            'next': self.next
        }
