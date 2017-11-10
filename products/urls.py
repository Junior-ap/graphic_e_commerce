from django.conf.urls import url
from . import views, views_dashboard

urlpatterns = [
    #Url de produtos
    url(r'^$', views_dashboard.list_product_view, name="list_product"),
    url(r'^novo-produto/$', views_dashboard.create_product_view, name="new_product"),
    url(r'^detalhar-produto/(?P<pk>\d+)$', views_dashboard.detail_product_view, name='detail_product'),

]
