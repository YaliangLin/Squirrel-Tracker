"""squirrel URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views
from .models import biaoge
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.mainmenu),
    path('map/',views.map),
    #path('sightings/<str:squirrel_id>/', views.goodview),
    path('sightings/add/',views.add),
    path('success/',views.success),
    re_path(r'^search/$', views.search, name='search'),
    path('sightings/',views.sightings),
    path('sightings/stats/',views.stats),
    path('sightings/<str:squirrel_id>/', views.edit),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)