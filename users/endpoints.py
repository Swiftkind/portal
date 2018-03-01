from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from users.api import UserViewSet


urlpatterns = format_suffix_patterns([
    path('users/<int:id>/', UserViewSet.as_view({'get': 'users_detail'}),
                                                name='users_detail'),
    path('users/update_profile/', UserViewSet.as_view({'put': 'update_users'}),
                                                name='update_users')
])
