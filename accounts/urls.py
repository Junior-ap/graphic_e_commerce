from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    #Login
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page':'accounts:login'}, name='logout'),
    #Usuario_Session
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    #Usuarios_Plataforma
    url(r'^newUser/$', views.create_user, name='new_user'),
    url(r'^list/$', views.list_user, name='list'),
    url(r'^detail/(?P<pk>\d+)$', views.detail_user, name='detail'),
    #Status_User
    url(r'^status/(?P<pk>\d+)/active', views.active, name='active'),
    url(r'^status/(?P<pk>\d+)/disable', views.disable, name='disable'),
    url(r'^status/(?P<pk>\d+)/block', views.block, name='block'),
    #Nivel_User
    url(r'^status/(?P<pk>\d+)/adm', views.adm, name='adm'),
    url(r'^status/(?P<pk>\d+)/salesman', views.salesman, name='salesman'),
    url(r'^status/(?P<pk>\d+)/customer', views.customer, name='customer'),
    #url(r'^new/', views.new, name='new'),
]
