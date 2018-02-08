from django.urls import path
from django.contrib.auth.views import login, logout
from . import views, views_dashboard


app_name = 'accounts'
urlpatterns = [
    #Login
    path('login/', login, {'template_name': 'login.html'}, name='login'),
    path('logout/', logout, {'next_page':'accounts:login'}, name='logout'),
    #Usuario_Session
    path('upload-img/', views_dashboard.upload_view, name='upload-img'),
    path('profile/', views_dashboard.profile, name='profile'),
    path('configuracao/', views_dashboard.settings_view, name='configuracao'),
    #Usuarios_Plataforma
    path('novo-usuario/', views_dashboard.create_user, name='new_user'),
    path('lista-usuarios/', views_dashboard.list_user, name='list_user'),
    path('detalhar-usuario/<int:pk>/cadastrado', views_dashboard.detail_user_taxed, name='detail_user_cadastrado'),
    #Status_User
    path('status/<int:pk>/active', views_dashboard.active, name='active'),
    path('status/<int:pk>/disable', views_dashboard.disable, name='disable'),
    path('status/<int:pk>/block', views_dashboard.block, name='block'),
    #Nivel_User
    path('nivel/<int:pk>/adm', views_dashboard.adm, name='adm'),
    path('nivel/<int:pk>/salesman', views_dashboard.salesman, name='salesman'),
    path('nivel/<int:pk>/customer', views_dashboard.customer, name='customer'),

]
