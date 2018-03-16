from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include

from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('invoices.urls')),
    path('api/', include('invoices.endpoints')),
    path('api/', include('users.endpoints')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    re_path('(.*)', TemplateView.as_view(template_name='base.html'), name='base'),
]