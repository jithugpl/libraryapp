"""
URL configuration for libraryapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from books import views
from rest_framework.authtoken import views as rviews #module aliasing
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('books',views.bookviewset)
router.register('user',views.userviewset)

urlpatterns = [
    path('admin/', admin.site.urls),
#    path('',views.booklist),
#    path('',views.Booklist.as_view()),
#    path('books/<int:pk>',views.BookDetail.as_view()),
    path('',include(router.urls)),
    path('api-token-auth/',rviews.obtain_auth_token),


]
