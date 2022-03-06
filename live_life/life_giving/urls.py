from django.contrib import admin
from django.urls import path , include
from  .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('/signup/' ,signup , name='signup'),
    path('login_user/' , login_user , name='login_user'),
    path('logout_user/' , logout_user , name='logout_user'),
    path('' , index , name='index'),
    path('donate_page/' , donate , name='donate_page' ),
    path('donate_form/<id>/' , donate_form , name='donate_form'),
    path('about/' , about , name='about'),
    path('raise/' , raise_exception , name='raise'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)