from django.conf.urls import url
from . import views ,viewsdashboard

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'dashboard/$', viewsdashboard.dashboard, name="dashboard"),
    url(r'carinho-compras/$', viewsdashboard.list_cart_item, name="list_cart"),
    url(r'^adicionar-produto/(?P<pk>\d+)$', viewsdashboard.add_card_item, name="add"),
]
