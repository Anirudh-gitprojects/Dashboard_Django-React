from django.contrib import admin

# add include to the path
from django.urls import path, include

# import views from todo
from . import views

# import routers from the REST framework
# it is necessary for routing
from rest_framework import routers

# create a router object
router = routers.DefaultRouter()
router.register(r'tasks', views.TodoView, 'task')
# register the router
urlpatterns=[
    path('api/', include(router.urls)),

]