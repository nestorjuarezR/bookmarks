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
                                                    name='password_change_done'),
    
    #Reseteo de contraseña
    path('password-reset/', auth_views.PasswordResetView.as_view(
                                                    template_name="./account/password_reset_form.html"),
                                                    name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
                                                    template_name ="./account/password_reset_done.html"),
                                                    name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
                                                    template_name="./account/password_reset_confirm.html"),
                                                    name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordChangeDoneView.as_view(
                                                    template_name="./account/password_reset_complete.html"),
                                                    name='password_reset_complete'),
]
