from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, View, ListView
from django.core.urlresolvers import reverse_lazy
from .models import  Order, Cart
from products.models import Product



class DashboardView(TemplateView):
    template_name = 'dashboard.html'


class AddCartItemView(View):

    def get(self, request, pk):
        us = self.request.user
        ordem = Order.objects.filter(user=us.pk , status=0)
        print('oi 1')
        if not ordem:
            Order.objects.create(user=us)
            return redirect(reverse_lazy('store:add', kwargs={'pk':pk}))
        else:
            ordem = Order.objects.get(user=us.pk , status=0)
            prod = get_object_or_404(Product, pk=pk)
            cart = Cart.objects.filter(product=pk)
            if not cart:
                Cart.objects.create(amounts=1, value=prod.saleValue, product=prod, order=ordem)
                ordem.valueTotal = ordem.valueTotal + prod.saleValue
                ordem.save()
            else:
                cart_atu = Cart.objects.get(product=us.pk)
                cart_atu.amounts = cart_atu.amounts + cart_atu.amounts
                cart_atu.save()
                ordem.valueTotal = ordem.valueTotal + cart_atu.value
                ordem.save()
        return redirect(reverse_lazy('products:list_product'))

class ListCartItemView(ListView):
    model = Cart
    context_object_name = 'itens_cart'
    template_name = 'cart.html'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(ListCartItemView, self).get_context_data(**kwargs)
        us = self.request.user
        context['ord'] = Order.objects.get(user=us.pk , status=0)
        return context

    def get_queryset(self):
        us = self.request.user
        ordem = Order.objects.filter(user=us.pk , status=0)
        if not ordem:
            Order.objects.create(user=us)
        else:
            ordem = Order.objects.get(user=us.pk , status=0)
        queryset = Cart.objects.filter(order=ordem.pk)
        return queryset


dashboard = DashboardView.as_view()
add_card_item = AddCartItemView.as_view()
list_cart_item = ListCartItemView.as_view()
