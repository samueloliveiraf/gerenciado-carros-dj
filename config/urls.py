from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

from apps.cars import urls as urls_cars

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include(urls_cars)),
] + static(
    settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT
)
