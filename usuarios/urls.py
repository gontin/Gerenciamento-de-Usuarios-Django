from django.urls import path
from .views import register, login_view, logout_view, inicio, cadastro_perfil, cadastro_data, gerar_pdf

urlpatterns = [
    path('cadastro/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('', inicio, name='inicio'),
    path('attperfil/', cadastro_perfil, name='attperfil'),
    path('attdados/', cadastro_data, name='attdata'),
    path('gerar_pdf/', gerar_pdf, name='gerar_pdf'),
]

