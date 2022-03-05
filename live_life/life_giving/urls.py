from django.contrib import admin
from django.urls import path , include
from  .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('index/' , index , name='index'),
    path('donate_page/' , donate , name='donate_page' ),
    path('about/' , about , name='about'),
    path('' ,signup , name='signup'),
    path('login_user/' , login_user , name='login_user'),
    path('raise/' , raise_exception , name='raise'),
    path('donate_form/<id>/' , donate_form , name='donate_form'),
    path('logout_user/' , logout_user , name='logout_user'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)