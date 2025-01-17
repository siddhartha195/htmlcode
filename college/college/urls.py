"""
URL configuration for college project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path("", views.index2, name="index2.urls"),
    path('index2',views.index2,name="index2.urls"),
    path('contact',views.contact,name="contact.urls"),
    path('singup',views.singup,name="singup.urls"),
    path('login',views.login,name="login.urls"),
    path('about',views.about,name="s.html.urls"),
    path('index',views.index,name="index.html.urls"),
    path('news',views.news,name="neme.html.urls"),
    path('contact',views.contact,name="contact.html.urls"),
    path('profile',views.profile,name="profile.html"),

    #path('about',views.about,name="about.urls"),
    #path("dashboard",include("dashboard.url")),
]
