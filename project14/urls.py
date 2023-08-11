"""
URL configuration for project14 project.

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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('table1/',table1,name='table1'),
    path('table2/',table2,name='table2'),
    path('table3/',table3,name='table3'),
    path('table4/',table4,name='table4'),
    path('table5/',table5,name='table5'),
    path('table6/',table6,name='table6'),
    path('table7/',table7,name='table7'),
    path('divtag1/',divtag1,name='divtag1'),
    path('divtag2/',divtag2,name='divtag2'),
    path('divtag3/',divtag3,name='divtag3'),
    path('forms1/',forms1,name='forms1'),
    path('forms2/',forms2,name='forms2'),
    path('forms3/',forms3,name='forms3'),
    path('imagetag/',imagetag,name='imagetag'),
    path('loginform/',loginform,name='loginform'),
    path('signupform/',signupform,name='signupform'),


]
