from django.contrib import admin
from django.urls import path, re_path, include
#from firstapp.article import views
from . import views
from django.contrib.auth import views as auth_views

app_name = 'loginsys'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),


    path('password_reset/', auth_views.password_reset,
         {
            'post_reset_redirect': '/auth/password_reset/done/',
             'email_template_name': 'password_reset_email.txt',
            'template_name': 'password_reset_form.html'
         }, name='password_reset'),
    path('password_reset/done/', auth_views.password_reset_done,
         {'template_name': 'password_reset_done.html'},
         name='password_reset_done'),

    #re_path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
    path('reset/<uidb64>/<token>/',
        auth_views.password_reset_confirm,
            name='password_reset_confirm'),
    path('reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),
    path('', include('django.contrib.auth.urls')),

]