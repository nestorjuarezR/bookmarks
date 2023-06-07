from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    #Login de usuario
    path('login/', auth_views.LoginView.as_view(
                                                template_name = "./account/login.html"),
                                                name= 'login'),
]
