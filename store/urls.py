from django.urls import path
from . import views ,views_dashboard

app_name = 'store'
urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views_dashboard.dashboard, name="dashboard"),
    path('minhas-ordens/', views_dashboard.my_order, name="minhas-ordens"),
    path('lista-ordens/', views_dashboard.list_order, name="listar-ordens"),
    path('finalizar-ordem/<int:pk>', views_dashboard.finalize_order, name="finalizar"),
    path('detalhar-ordem/<int:pk>', views_dashboard.detail_order, name="detail_order"),
    path('status/<int:pk>/finalizar', views_dashboard.finalize_status, name='finalizar_status'),
    path('status/<int:pk>/entregue', views_dashboard.delivered_status, name='entregue_status'),
    path('status/<int:pk>/fabricar', views_dashboard.factory_status, name='fabricar_status'),
    #Urls Cart
    path('carinho-compras/', views_dashboard.list_cart_item, name="list_cart"),
    path('deleta-item/<int:pk>', views_dashboard.delete_cart_item, name="delete_item"),
    path('somar-item/<int:pk>', views_dashboard.sum_cart_item, name="somar_item"),
    path('subitrair-item/<int:pk>', views_dashboard.subtract_cart_item, name="subitrair_item"),
    path('adicionar-produto/<int:pk>', views_dashboard.add_card_item, name="add"),
]
