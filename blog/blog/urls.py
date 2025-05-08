
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login_page/', views.login_page, name='login_page'),
    path('register_page/', views.register_page, name='register_page'),

    path('all_blogs/', include('all_blogs.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
