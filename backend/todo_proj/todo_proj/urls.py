"""todo_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from todo import views

users_list = views.UserViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
#router.register(r'todo', views.TODOViewSet, basename='TODOViewSet')

api_urls = [
    path(r'status/', views.Userstatus.as_view()),
    path(r'user_login/', views.user_login.as_view()),
    path(r'user_logout/', views.user_logout.as_view()),
    path(r'todo/', views.TODOView.as_view()),
    path('todo/<int:pk>/', views.TODOView.as_view()),
]

urlpatterns = [
    path(r'api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls)),
]
