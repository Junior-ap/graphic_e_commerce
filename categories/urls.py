from django.urls import path
from . import views

app_name = 'catefories'
urlpatterns = [
    path('nova-categoria/', views.create_category, name='new_category'),
    path('lista-categoria/', views.list_category, name='list_categories'),
    path('detalhar-categoria/<int:pk>', views.detail_category, name='detail_category'),
]
