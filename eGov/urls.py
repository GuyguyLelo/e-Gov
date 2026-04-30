"""
URL configuration for eGov project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import RedirectView
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/login/', permanent=False)),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', views.home, name='home'),
    path('parametres/utilisateurs/', views.user_management, name='user_management'),
    path('parametres/bases/', views.database_management, name='database_management'),
    path('civil/', views.civil_search, name='civil_search'),
    path('police/', views.police_search, name='police_search'),
    path('police/detail/', views.police_detail, name='police_detail'),
    path('police/detail/pdf/', views.police_detail_pdf, name='police_detail_pdf'),
    path('civil/detail/', views.civil_detail, name='civil_detail'),
    path('civil/detail/pdf/', views.civil_detail_pdf, name='civil_detail_pdf'),
    path('civil/communes/', views.civil_communes_api, name='civil_communes_api'),
]
