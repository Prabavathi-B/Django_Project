"""
URL configuration for Django_Project project.

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
from Food_Recipes import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home),
    path('recipecategory',views.recipecategory,name='recipecategory'),
    path('lunch',views.lunch,name='lunch'),
    path('admin/', admin.site.urls),
    path('breakfast_details/', views.breakfast_detail, name='breakfast_details'),
    path('dinner_details/', views.dinner_detail, name='dinner_details'),
    path('juice_details/', views.juice_detail, name='juice_details'),
    path('sweet_details/', views.sweet_detail, name='sweet_details'),
    path('breakfast/<int:id>/', views.breakfast_view, name='breakfast_view'),
    path('dinner/<int:id>/', views.dinner_view, name='dinner_view'),
    path('juice/<int:id>/', views.juice_view, name='juice_view'),
    path('sweet/<int:id>/', views.sweet_view, name='sweet_view'),
    
    
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)