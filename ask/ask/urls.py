"""ask URL Configuration

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
from django.conf.urls import url, include
from qa.views import get_popular, test, get_page, ask, signup, login_view

urlpatterns = [
    url(r'login/', login_view),
    url(r'^$', get_page),
    url(r'signup/', signup),
    url(r'ask/', ask),
    url(r'popular/', get_popular),
    url(r'question/', include('qa.urls')),
   
]
