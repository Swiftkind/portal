from django.urls import path

from users.views import UserAPI


urlpatterns = [
    path('auth/', UserAPI.as_view({
        'get': 'detail',
        'post': 'update',
        }), name='user-auth')
]
