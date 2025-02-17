"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
# , re_path
from django.contrib import admin
# from django.contrib.auth import views as auth_views
# from users.views import CustomLoginView, ResetPasswordView, ChangePasswordView

# from users.forms import LoginForm

# Use include() to add URLS from the catalog application and authentication system
from django.urls import include

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
    
    path('accounts/', include('users.urls')),
    path('', RedirectView.as_view(url='/users/', permanent=True)),

    path('store/', include('store.urls')),
    path('', RedirectView.as_view(url='/store/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


