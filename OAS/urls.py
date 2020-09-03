
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="homepage"),
    path('organizations/', include('apps.Organizations.urls')),
    path('users/', include('apps.Users.urls')),
    path('register/', views.register, name="registerpage"),
    path('login/', views.loginpage, name="loginpage"),
    path('logout/', views.logoutpage, name="logoutpage"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
