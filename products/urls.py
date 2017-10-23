from django.conf.urls import url
from . import views

urlpatterns = [
    #Url de produtos
    url(r'^$', views.list_product_view, name="list_product"),
    url(r'^novo-produto/$', views.create_product_view, name="new_product"),
    url(r'^detalhar-produto/(?P<pk>\d+)$', views.detail_product_view, name='detail_product'),
    
]
