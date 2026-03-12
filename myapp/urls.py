"""
URL configuration for railwayobjectdetection project.

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
from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('login_get/',views.login_get),
    path('login_post/',views.login_post),
    path('forgotpassword_get/',views.forgotpassword_get),
    path('forgotpassword_post/',views.forgotpassword_post),
    # admin-----
    path('add_authority_get/', views.add_authority_get),
    path('add_authority_post/', views.add_authority_post),
    path('change_password_get/', views.change_password_get),
    path('change_password_post/', views.change_password_post),
    path('edit_authority_get/<id>', views.edit_authority_get),
    path('edit_authority_post/', views.edit_authority_post),
    path('sendreply_get/<id>', views.sendreply_get),
    path('sendreply_post/', views.sendreply_post),
    path('viewauthority_get/', views.viewauthority_get),
    path('viewblockedusers_get/', views.viewblockedusers_get),
    path('viewcomplaint_get/', views.viewcomplaint_get),
    path('viewlogs_get/', views.viewlogs_get),
    path('viewuser_get/', views.viewuser_get),
    path('admin_home/',views.admin_home),
    path('blockeduser/<id>',views.blockeduser),
    path('logout_get/',views.logout_get),
    path('delete_authority/<id>',views.delete_authority),
    path('add_police_get/', views.add_police_get),
    path('add_police_post/', views.add_police_post),
    path('viewpolice_get/', views.viewpolice_get),
    path('delete_police/<id>', views.delete_police),
    path('edit_police_get/<id>', views.edit_police_get),
    path('edit_police_post/', views.edit_police_post),
    path('admin_viewcriminaldetection_get/', views.admin_viewcriminaldetection_get),

    # authority---
    path('authority_home/',views.authority_home),
    path('edit_profile_get/', views.edit_profile_get),
    path('edit_profile_post/', views.edit_profile_post),
    path('manage_criminals_get/', views.manage_criminals_get),
    path('manage_criminals_post/', views.manage_criminals_post),
    path('register_authority_get/', views.register_authority_get),
    path('register_authority_post/', views.register_authority_post),
    path('sendcomplainttoadmin_get/', views.sendcomplainttoadmin_get),
    path('sendcomplainttoadmin_post/', views.sendcomplainttoadmin_post),
    path('sendreplytopolice_get/<id>', views.sendreplytopolice_get),
    path('sendreplytopolice_post/', views.sendreplytopolice_post),
    path('viewcomplaintpolice_get/', views.viewcomplaintpolice_get),
    path('viewcriminaldetection_get/', views.viewcriminaldetection_get),
    path('viewcriminals_get/', views.viewcriminals_get),
    path('viewobjectdetection_get/', views.viewobjectdetection_get),
    path('viewpolicestaff_get/', views.viewpolicestaff_get),
    path('viewprofile_get/', views.viewprofile_get),
    path('viewreply_get/', views.viewreply_get),
    path('a_change_password_get/',views.a_change_password_get),
    path('a_change_password_post/',views.a_change_password_post),
    path('a_viewcomplaint_get/',views.a_viewcomplaint_get),
    path('a_sendreply_get/',views.a_sendreply_get),
    path('a_sendreply_post/',views.a_sendreply_post),
    path('delete_criminal/<id>',views.delete_criminal),
    path('edit_criminal_get/<id>',views.edit_criminal_get),
    path('edit_criminal_post/',views.edit_criminal_post),


    # police---
    path('register_police_get/', views.register_police_get),
    path('register_police_post/', views.register_police_post),
    path('sendcomplaintpolice_get/', views.sendcomplaintpolice_get),
    path('sendcomplaintpolice_post/', views.sendcomplaintpolice_post),
    path('viewcriminaldetectionpolice_get/', views.viewcriminaldetectionpolice_get),
    path('viewobjectdetectionpolice_get/', views.viewobjectdetectionpolice_get),
    path('viewreplypolice_get/', views.viewreplypolice_get),


    #app---
    path('app_login_post/',views.app_login_post),
    path('app_view_profile/',views.app_view_profile),
    path('app_change_password_post/',views.app_change_password_post),
    path('app_sendcomplaint_post/',views.app_sendcomplaint_post),
    path('app_viewreply_get/',views.app_viewreply_get),
    path('app_viewobjectdetectionpolice_get/',views.app_viewobjectdetectionpolice_get),
    path('app_viewcriminaldetectionpolice_get/',views.app_viewcriminaldetectionpolice_get),

]
