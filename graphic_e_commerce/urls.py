from django.urls import path, include


urlpatterns = [
    path('', include('store.urls', namespace='stores')),
    path('account/', include('accounts.urls', namespace='accounts')),
    path('address/', include('address.urls', namespace='address')),
    path('categorias/', include('categories.urls', namespace='categories')),
    path('products/', include('products.urls', namespace='products')),

]
