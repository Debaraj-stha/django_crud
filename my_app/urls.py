from django.contrib import admin
from django.urls import path,include
from my_app import views
urlpatterns = [
    path('about', views.about,name="about"),
    path('services', views.services,name="services"),
    path('', views.home,name="home"),
    path('contact', views.contact,name="contact"),
    path('all-contacts', views.getAllContact,name="myContact"),
    path('logout', views.logout,name="logout"),
    path('update-contact', views.updateContact, name='updatecontact'),
    path('delete-contact/<int:id>', views.deleteContact, name="deletecontact"),
]