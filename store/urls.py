from django.conf.urls import url
from . import views ,views_dashboard

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'dashboard/$', views_dashboard.dashboard, name="dashboard"),
    url(r'minhas-ordens/$', views_dashboard.my_order, name="minhas-ordens"),
    url(r'finalizar-ordem/(?P<pk>\d+)$', views_dashboard.finalize_order, name="finalizar"),
    url(r'detalhar-ordem/(?P<pk>\d+)$', views_dashboard.detail_order, name="detail_order"),
    url(r'^status/(?P<pk>\d+)/finalizar', views_dashboard.finalize_status, name='finalizar_status'),
    url(r'^status/(?P<pk>\d+)/entregue', views_dashboard.delivered_status, name='entregue_status'),
    url(r'^status/(?P<pk>\d+)/fabricar', views_dashboard.factory_status, name='fabricar_status'),
    #Urls Cart
    url(r'carinho-compras/$', views_dashboard.list_cart_item, name="list_cart"),
    url(r'deleta-item/(?P<pk>\d+)$', views_dashboard.delete_cart_item, name="delete_item"),
    url(r'somar-item/(?P<pk>\d+)$', views_dashboard.sum_cart_item, name="somar_item"),
    url(r'subitrair-item/(?P<pk>\d+)$', views_dashboard.subtract_cart_item, name="subitrair_item"),
    url(r'^adicionar-produto/(?P<pk>\d+)$', views_dashboard.add_card_item, name="add"),
]
