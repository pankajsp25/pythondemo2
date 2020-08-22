from django.urls import path, include
from accounts.views import AccountCreateView

app_name = 'accounts'

urlpatterns = [
    path('register/', AccountCreateView.as_view(), name='register'),
    path('accounts/', include('rest_registration.api.urls')),
]
