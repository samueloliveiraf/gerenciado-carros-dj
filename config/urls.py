from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from apps.cars import urls as urls_cars

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', include(urls_cars)),
] + static(
    settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT
)
