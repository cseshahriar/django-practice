from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tfa.urls')),
    path('', include('csvapp.urls')),
    path('', include('djorm.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
