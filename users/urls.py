from django.urls import path


from users import views


urlpatterns = [
    path('user/dashboard/', views.DashboardView.as_view(), name='dashboard'),
]