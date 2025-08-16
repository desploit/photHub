from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('home/', views.Home_page, name='home'),
    path('add/', views.Add_post, name='add'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('picture/<int:pk>/', views.view_picture, name='picture'),
    path('system/', views.admin_page, name='system'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)