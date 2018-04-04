from django.urls import path
from users.views import UserAPI, AuthAPI


urlpatterns = [
    path('auth/', UserAPI.as_view({
        'get': 'detail',
        'post': 'update',
        }), name='user_auth'),
    path('login/', AuthAPI.as_view({
        'post': 'login',
        }), name='login'),
    path('logout/', AuthAPI.as_view({
        'get': 'logout',
        }), name='logout'),
    path('register/', AuthAPI.as_view({
        'post': 'register',
        }), name='register'),
]
