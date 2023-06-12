from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    #Login de usuario
    path('login/', auth_views.LoginView.as_view(
                                                template_name = "./account/login.html"),
                                                name= 'login'),
    path('logout/', auth_views.LogoutView.as_view(
                                                    next_page = "/"),
                                                    name="logout"),
    #Cambio de contraseña
    path('password-change/', auth_views.PasswordChangeView.as_view(
                                                    template_name = "./account/password_change_form.html"),
                                                    name='password_change'),
    #Correcto cambio de contraseña
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(
                                                    template_name = "./account/password_change_done.html"),
                                                    name='password_change_done')
]
