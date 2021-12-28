"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
import templateproject.views
from django.conf import settings 
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',templateproject.views.test),
    url(r'^index', templateproject.views.test, name = "index_url"),
    url(r'^gallery', templateproject.views.gallery, name = "gallery_url"),
    url(r'^contact', templateproject.views.contact, name = "contact_url"),
    url(r'^about', templateproject.views.about, name = "about_url"),
    url(r'^services', templateproject.views.services, name = "services_url"),
    url(r'^single', templateproject.views.single, name = "single_url"),
    url(r'^register', templateproject.views.register, name ="register_url"),
    url(r'^login', templateproject.views.login, name = "login_url"),
    
    
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
