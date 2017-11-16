from django.conf.urls import url
from . import views, views_dashboard

urlpatterns = [
    #Url de Gallery Products
    url(r'^galeria-imgens/(?P<pk>\d+)$', views_dashboard.gallery_product_view, name='galeria-imagens'),
    url(r'^upload-img/(?P<pk>\d+)$', views_dashboard.upload_img_product_view, name='upload-img'),
    url(r'^img-deleta/(?P<pk>\d+)$', views_dashboard.gallery_img_delete_view, name='img-deletar'),
    url(r'^img-padrao/(?P<pk>\d+)$', views_dashboard.gallery_img_defalt_view, name='img-padrao'),
    #Url de produtos
    url(r'^$', views_dashboard.list_product_view, name="list_product"),
    url(r'^novo-produto/$', views_dashboard.create_product_view, name="new_product"),
    url(r'^detalhar-produto/(?P<pk>\d+)$', views_dashboard.detail_product_view, name='detail_product'),

]
