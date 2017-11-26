from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views, views_dashboard

urlpatterns = [
    #Login
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page':'accounts:login'}, name='logout'),
    #Usuario_Session
    url(r'^upload-img/$', views_dashboard.upload_view, name='upload-img'),
    url(r'^profile/$', views_dashboard.profile, name='profile'),
    url(r'^configuracao/$', views_dashboard.settings_view, name='configuracao'),
    #Usuarios_Plataforma
    url(r'^novo-usuario/$', views_dashboard.create_user, name='new_user'),
    url(r'^lista-usuarios/$', views_dashboard.list_user, name='list_user'),
    url(r'^detalhar-usuario/(?P<pk>\d+)/cadastrado$', views_dashboard.detail_user_taxed, name='detail_user_cadastrado'),
    #Status_User
    url(r'^status/(?P<pk>\d+)/active', views_dashboard.active, name='active'),
    url(r'^status/(?P<pk>\d+)/disable', views_dashboard.disable, name='disable'),
    url(r'^status/(?P<pk>\d+)/block', views_dashboard.block, name='block'),
    #Nivel_User
    url(r'^nivel/(?P<pk>\d+)/adm', views_dashboard.adm, name='adm'),
    url(r'^nivel/(?P<pk>\d+)/salesman', views_dashboard.salesman, name='salesman'),
    url(r'^nivel/(?P<pk>\d+)/customer', views_dashboard.customer, name='customer'),
    #url(r'^new/', views.new, name='new'),
]
