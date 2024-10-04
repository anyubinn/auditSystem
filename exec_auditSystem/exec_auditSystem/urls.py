"""
URL configuration for exec_auditSystem project.

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
from django.urls import path

import auditSystem.views

app_name='exec_auditSystem'
urlpatterns = [
    path('', auditSystem.views.index, name='index'),
    path('main/', auditSystem.views.main, name='main'),
    path('signin/', auditSystem.views.signin, name='signin'),
    path('statusReview/', auditSystem.views.statusReview, name='statusReview'),
    path('profile/', auditSystem.views.profile, name='profile'),
    path('profile/<int:emp_id>/', auditSystem.views.personal, name='personal'),
    path('admin/', auditSystem.views.admin, name='admin'),
    path('signout/', auditSystem.views.signout, name='signout'),
    path('search/', auditSystem.views.search, name='search'),
    path('result/', auditSystem.views.result, name='result')
]
