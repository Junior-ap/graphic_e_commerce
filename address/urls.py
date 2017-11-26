from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.new, name="new"),
    url(r'excluir/(?P<pk>\d+)$', views.delete, name='excluir'),
]
