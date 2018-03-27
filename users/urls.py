from django.urls import path
from users.views import UserAPI, LoginAPI


urlpatterns = [
    path('auth/', UserAPI.as_view({
        'get': 'detail',
        'post': 'update',
        }), name='user_auth'),
    path('login/', LoginAPI.as_view({
        'post': 'post',
        }), name='login'),
]
