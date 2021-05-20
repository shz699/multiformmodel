"""multiformmodel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django import conf
from django.contrib import admin
from django.urls import path , include
from my_app.views import index ,landing , submitted , UpdateExist , Ex_User
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing , name='landing'),
    path('index/', index , name='index' ),
    path('my_app/', include('my_app.urls' , namespace='my_app')),
    path('index/ex_user/', Ex_User , name='ex_user' ),
    path('submitted/', submitted , name='submitted' ),
]

urlpatterns += static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)
