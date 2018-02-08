from django.urls import path
from . import views


app_name = 'address'
urlpatterns = [
    path('', views.new, name="new"),
    path('excluir/int:<pk>', views.delete, name='excluir'),
]
