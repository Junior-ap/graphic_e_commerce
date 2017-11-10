from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, View, ListView, DetailView

from datetime import date

from .models import  Order, Cart
from .forms import OrderCreationdeForm

from products.models import Product
from accounts.polices import IsSalesMan


class DashboardView(LoginRequiredMixin, IsSalesMan, ListView):
    model = Order
    context_object_name = 'order'
    template_name = 'dashboard.html'
    paginate_by = 10

    def get_queryset(self):
        filtro = self.request.GET.get('filtro')
        if filtro is not None:
            if filtro == 'finalizada':
                queryset = Order.objects.filter(status=1)
            if filtro == 'entregue':
                queryset = Order.objects.filter(status=3)
            if filtro == 'fabricar':
                queryset = Order.objects.filter(status=2)
        else:
            queryset = Order.objects.filter(status=2)
        return queryset

class AddCartItemView(LoginRequiredMixin, IsSalesMan, View):

    def get(self, request, pk):
        us = self.request.user
        ordem = Order.objects.filter(user=us.pk , status=0)
        if not ordem:
            Order.objects.create(user=us)
            return redirect(reverse_lazy('store:add', kwargs={'pk':pk}))
        else:
            ordem = Order.objects.get(user=us.pk , status=0)
            prod = get_object_or_404(Product, pk=pk)
            cart = Cart.objects.filter(product=pk, order= ordem.pk)
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
        return redirect(reverse_lazy('store:list_cart'))

class ListCartItemView(LoginRequiredMixin, IsSalesMan, ListView):
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

class DeleteCartItemView(LoginRequiredMixin, IsSalesMan, View):

    def get(self, request, pk):
        us = self.request.user
        ordem = Order.objects.get(user=us.pk, status=0)
        item = Cart.objects.get(pk=pk)
        ordem.valueTotal = ordem.valueTotal - (item.amounts * item.value)
        ordem.save()
        item.delete()
        return redirect(reverse_lazy('store:list_cart'))

class SumCartItemView(LoginRequiredMixin, IsSalesMan, View):

    def get(self, request, pk):
        us = self.request.user
        ordem = Order.objects.get(user=us.pk, status=0)
        item = Cart.objects.get(pk=pk)
        item.amounts = item.amounts + 1
        ordem.valueTotal = ordem.valueTotal + item.value
        ordem.save()
        item.save()
        return redirect(reverse_lazy('store:list_cart'))

class SubtractCartItemView(LoginRequiredMixin, IsSalesMan, View):

    def get(self, request, pk):
        us = self.request.user
        ordem = Order.objects.get(user=us.pk, status=0)
        item = Cart.objects.get(pk=pk)
        item.amounts = item.amounts - 1
        ordem.valueTotal = ordem.valueTotal - item.value
        ordem.save()
        item.save()
        return redirect(reverse_lazy('store:list_cart'))

class FinalizeOrderView(LoginRequiredMixin, IsSalesMan, View):

    def get(self, request, pk):
        ordem = Order.objects.get(pk=pk)
        endDate = date.fromordinal(ordem.dateStart.toordinal() + 5)
        ordem.dateEnd = endDate
        ordem.status = 2
        ordem.save()
        return redirect(reverse_lazy('store:dashboard'))

class ChangeStatusOrderView(LoginRequiredMixin, IsSalesMan, View):
    status = 2
    def get(self, request, pk):
        ordem = get_object_or_404(Order, pk=pk)
        ordem.status = self.status
        ordem.save()
        return redirect(reverse_lazy('store:detail_order', kwargs={'pk':ordem.pk}))

class DetailOrderView(LoginRequiredMixin, IsSalesMan, DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'detail_order.html'

    def get_context_data(self, **kwargs):
        context = super(DetailOrderView, self).get_context_data(**kwargs)
        context['form'] = OrderCreationdeForm(self.request.POST or None, instance=context['order'])
        context['ord'] = Order.objects.get(pk=self.kwargs['pk'])
        context['cart_items'] = Cart.objects.filter(order=self.kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        form = context['form']
        if form.is_valid():
            form.save()
        return redirect(reverse_lazy('store:detail_order', kwargs={'pk':self.get_object().pk}))


dashboard = DashboardView.as_view()
finalize_order = FinalizeOrderView.as_view()
detail_order = DetailOrderView.as_view()
finalize_status = ChangeStatusOrderView.as_view(status=1)
factory_status = ChangeStatusOrderView.as_view(status=2)
delivered_status = ChangeStatusOrderView.as_view(status=3)
#Cart Views
add_card_item = AddCartItemView.as_view()
list_cart_item = ListCartItemView.as_view()
delete_cart_item = DeleteCartItemView.as_view()
sum_cart_item = SumCartItemView.as_view()
subtract_cart_item = SubtractCartItemView.as_view()
