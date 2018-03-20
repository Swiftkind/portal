from django.urls import path
from users.views import DashboardView, LoginView, UserAPI


urlpatterns = [
    path('auth/', UserAPI.as_view({
        'get': 'detail',
        'post': 'update',
        }), name='user-auth')
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]






