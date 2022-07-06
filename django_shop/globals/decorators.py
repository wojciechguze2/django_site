from django.http import JsonResponse
from rest_framework import status


def exceptions_debugger():
    """
    Prints exception in console
    """
    def decorator(func):
        def inner(request, *args, **kwargs):
            try:
                return func(request, *args, **kwargs)
            except Exception as e:
                print(e)

                response = {
                    'reason': 'Exception',
                    'detail': repr(e),
                }

                if hasattr(e, 'http_status'):
                    response_status = e.http_status
                elif hasattr(e, 'status_code'):
                    response_status = e.status_code
                else:
                    response_status = status.HTTP_500_INTERNAL_SERVER_ERROR

                return JsonResponse(
                    response,
                    safe=False,
                    status=response_status
                )

        return inner

    return decorator
