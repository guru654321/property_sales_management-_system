"""
URL configuration for propertysalepro project.

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
from propertysaleapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('logout_view',views.logout_view,name='logout_view'),
    path('home',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('clientdata',views.clientdata,name='clientdata'),
    path('registration',views.registration,name='registration'),
    path('afterlogin',views.afterlogin,name='afterlogin'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('new_property_data',views.new_property_data,name='new_property_data'),
    path('display_properties',views.display_properties,name='display_properties'),
    path('newpropertytype',views.newpropertytype,name='newpropertytype'),
    path('addstatusname',views.addstatusname,name='addstatusname'),
    path('CustomerDashboard',views.CustomerDashboard,name='CustomerDashboard'),
    path('edit_property/<int:id>/', views.edit_property, name='edit_property'),
    path('delete/<int:id>/',views.delete_property, name='delete_property'),
    path('delete_property/<int:id>/',views.delete_property, name='delete_property'),

    path('type_report/edit/<int:id>/',views.edit_type, name='edit_type'),\
    path('type_report',views.type_report,name='type_report'),


    path('statusreports',views.statusreports,name='statusreports'),
    path('edit_status/<int:id>/', views.edit_status, name='edit_status'),
    path('delete_status/<int:id>/', views.delete_status, name='delete_status'),

    path('all_property', views.all_property, name='all_property'),



]
