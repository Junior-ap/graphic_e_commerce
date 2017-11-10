from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    #Login
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page':'accounts:login'}, name='logout'),
    #Usuario_Session
    url(r'^profile/(?P<pk>\d+)$', views.profile, name='profile'),
    #Usuarios_Plataforma
    url(r'^novo-usuario/$', views.create_user, name='new_user'),
    url(r'^lista-usuarios/$', views.list_user, name='list_user'),
    url(r'^detalhar-usuario/(?P<pk>\d+)/cadastrado$', views.detail_user_taxed, name='detail_user_cadastrado'),
    #Status_User
    url(r'^status/(?P<pk>\d+)/active', views.active, name='active'),
    url(r'^status/(?P<pk>\d+)/disable', views.disable, name='disable'),
    url(r'^status/(?P<pk>\d+)/block', views.block, name='block'),
    #Nivel_User
    url(r'^nivel/(?P<pk>\d+)/adm', views.adm, name='adm'),
    url(r'^nivel/(?P<pk>\d+)/salesman', views.salesman, name='salesman'),
    url(r'^nivel/(?P<pk>\d+)/customer', views.customer, name='customer'),
    #url(r'^new/', views.new, name='new'),
]
