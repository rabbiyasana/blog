
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from .views import views
from .views.post_views import create_post,delete_post,edit_post
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login_page/', views.login_page, name='login_page'),
    path('register_page/', views.register_page, name='register_page'),
    path('logout_page/', views.logout_page, name='logout_page'),
    path('verify-email/', views.verify_email, name='verify_email'),

    path('forgot-password/', auth_views.PasswordResetView.as_view(template_name='website/auth/forgot_password.html'), name='forgot_password'),
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name='website/auth/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='website/auth/password_reset_form.html'), name='password_reset_confirm'),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='website/auth/password_reset_done.html'), name='password_reset_complete'),
    
    path('create_post/', create_post.create_post, name='create_post'),
    path('delete_post/<int:blog_id>/', delete_post.delete_post, name='delete_post'),
    path('edit_post/<int:blog_id>/', edit_post.edit_post, name='edit_post'),
   


    path('all_blogs/', include('all_blogs.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
