from django.urls import path


from users.views  import DashboardView


urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]