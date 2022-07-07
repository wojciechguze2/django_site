class Pagination:
    def __init__(self, queryset, page_number: int = 1):
        if isinstance(queryset, list):
            self.queryset_count = len(queryset)
        else:
            self.queryset_count = queryset.count()

        self.limit = 5
        self.pages_count = self.queryset_count / self.limit
        self.page_number = page_number
        self.offset = (self.page_number - 1) * self.limit
        self.page_results = queryset[self.offset:self.offset + self.limit]
