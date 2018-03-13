from django.urls import path
from django.views.generic import TemplateView
from users.views import LoginView, DashboardView, UpdateProfileView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profile/', TemplateView.as_view(template_name='users/users_profile.html'), name='profile'),
    path('update_profile/', UpdateProfileView.as_view(), name='update_profile')
]
