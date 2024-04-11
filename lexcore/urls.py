"""
URL configuration for lexcore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from dashboard.views import *
from dashboard import views as dashboard_view


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('dashboard.urls')),
    path('', include('client.urls')),
    path('', include('casefolder.urls')),
    path('', include('matter.urls')),
    path('', include('activity.urls')),
    path('', include('reference_lookup.urls')),
    path('', include('invoice.urls')),
    path('', include('userprofile.urls')),
    path('', include('emailportal.urls')),
    path('', include('docutemplates.urls')),
    path('', include('chatter.urls')),
    path('', include('searchengine.urls')),
    path('', include('dataconversion.urls')),
    path('', include('tmwatch.urls')),

] 
#if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)


# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += staticfiles_urlpatterns()

# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

