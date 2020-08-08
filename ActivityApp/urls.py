from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('user_login', user_login, name="user_login"),
    path("validatemylogin",validatemylogin,name="validatemylogin"),
    path("dashboard",dashboard,name="dashboard"),
    path("add_user",add_user,name="add_user"),
    path("add_activity",add_activity,name="add_activity"),
    path("save_new_user_endpoint",save_new_user_endpoint,name="save_new_user_endpoint"),
    path("save_activity_endpoint",save_activity_endpoint,name="save_activity_endpoint"),
]
