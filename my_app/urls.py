
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from my_app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('about', views.about,name="about"),
    path('services', views.services,name="services"),
    path('', views.home,name="home"),
    path('contact', views.contact,name="contact"),
    path('all-contacts', views.getAllContact,name="myContact"),
    path('logout', views.logout,name="logout"),
    path('update-contact', views.updateContact, name='updatecontact'),
    path('signup', views.signUp,name="signup"),
    # path('login', views.Login,name="login"),
    path('delete-contact/<int:id>', views.deleteContact, name="deletecontact"),
    path('logout', views.logout,name="logout"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
