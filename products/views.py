from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, CreateView, ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy

from .forms import ProductCreationForm
from .models import Product
from categories.models import Category

class CreateProductView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductCreationForm
    template_name = 'create_products_dashboard.html'
    success_url = reverse_lazy('products:list_product')

class ListProductView(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'product'
    template_name = 'list_products_dashboard.html'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(ListProductView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

    def get_queryset(self):
        filtro = self.request.GET.get('filtro')
        if filtro is not None:
            queryset = Product.objects.filter(category=filtro)
        else:
            queryset = Product.objects.all()
        return queryset

class DetailProductView(TemplateView):
    template_name = 'detail_product_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DetailProductView, self).get_context_data(**kwargs)
        pk = kwargs['pk']
        product = get_object_or_404(Product, pk=pk)
        context['product'] = product
        context['form'] = ProductCreationForm(self.request.POST or None, instance=product)
        return context


create_product_view = CreateProductView.as_view()
list_product_view = ListProductView.as_view()
detail_product_view = DetailProductView.as_view()
