from django.urls import path
from django.contrib.auth import views as auth_views
from .models import Clientes
from . import views

urlpatterns = [

    path("cadastro/", views.cadastro, name="cadastro"),
    # Login e Logout
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", views.painel_controle, name="painel_controle"),

    # Alteradores de Senha 
    path("alterar_senha/", auth_views.PasswordChangeView.as_view(), name="password_change"),
    path("alterar_senhar/alterada", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
]