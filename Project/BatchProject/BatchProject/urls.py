from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin-site/', admin.site.urls), # Renamed to avoid conflict with custom admin
    path('', include('Userapp.urls')),
    path('custom-admin/', include('AdminApp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
