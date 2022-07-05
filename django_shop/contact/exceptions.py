from rest_framework import status


class ContactSaveError(Exception):
    def __init__(self):
        self.http_status = status.HTTP_409_CONFLICT
        super(ContactSaveError, self).__init__('Contact save error.')
