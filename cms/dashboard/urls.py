from django.urls import path

from cms.dashboard.views import DashboardViewSet

dashboard = DashboardViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('', dashboard, name='cms_dashboard')
]
