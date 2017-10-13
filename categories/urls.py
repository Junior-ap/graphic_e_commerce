from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^nova-categoria/$', views.create_category, name='new_category'),
    url(r'^lista-categoria/$', views.list_category, name='list_categories'),
    url(r'^detalhar-categoria/(?P<pk>\d+)$', views.detail_category, name='detail_category'),
]
