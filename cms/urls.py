from django.urls import include, re_path

urlpatterns = [
    re_path('', include('cms.dashboard.urls')),
]
