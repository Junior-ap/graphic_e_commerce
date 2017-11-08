from django.conf.urls import url
from . import views ,viewsdashboard

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'dashboard/$', viewsdashboard.dashboard, name="dashboard"),
    url(r'finalizar-ordem/(?P<pk>\d+)$', viewsdashboard.finalize_order, name="finalizar"),
    url(r'detalhar-ordem/(?P<pk>\d+)$', viewsdashboard.detail_order, name="detail_order"),
    url(r'^status/(?P<pk>\d+)/finalizar', viewsdashboard.finalize_status, name='finalizar_status'),
    url(r'^status/(?P<pk>\d+)/entregue', viewsdashboard.delivered_status, name='entregue_status'),
url(r'^status/(?P<pk>\d+)/fabricar', viewsdashboard.factory_status, name='fabricar_status'),
    #Urls Cart
    url(r'carinho-compras/$', viewsdashboard.list_cart_item, name="list_cart"),
    url(r'deleta-item/(?P<pk>\d+)$', viewsdashboard.delete_cart_item, name="delete_item"),
    url(r'somar-item/(?P<pk>\d+)$', viewsdashboard.sum_cart_item, name="somar_item"),
    url(r'subitrair-item/(?P<pk>\d+)$', viewsdashboard.subtract_cart_item, name="subitrair_item"),
    url(r'^adicionar-produto/(?P<pk>\d+)$', viewsdashboard.add_card_item, name="add"),
]
