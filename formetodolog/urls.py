"""formetodolog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from formetodolog import settings
#from formetodolog.loginsys.views import SignupView
from loginsys.views import SignupView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    #path('auth/', include('loginsys.urls')),
    path('account/login/', LoginView.as_view(), name="account_login"),
    path("account/signup/", SignupView.as_view(), name="account_signup"),
    path('account/', include("account.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


