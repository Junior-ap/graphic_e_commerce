from django.urls import path
from . import views, views_dashboard


app_name = 'products'
urlpatterns = [
    #Url de Gallery Products
    path('imagens/<int:pk>', views_dashboard.gallery_product_view, name='imagens'),
    path('upload-img/<int:pk>', views_dashboard.upload_img_product_view, name='upload-img'),
    path('img-deleta/<int:pk>', views_dashboard.gallery_img_delete_view, name='img-deletar'),
    path('img-padrao/<int:pk>', views_dashboard.gallery_img_defalt_view, name='img-padrao'),
    #Url de produtos
    path('', views_dashboard.list_product_view, name="list_product"),
    path('novo-produto/', views_dashboard.create_product_view, name="new_product"),
    path('detalhar-produto/<int:pk>', views_dashboard.detail_product_view, name='detail_product'),

]
