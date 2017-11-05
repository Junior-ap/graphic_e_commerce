from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView , TemplateView
from .models import Address
from .forms import AddressCreationForm
from django.core.urlresolvers import reverse_lazy


class CreateAdressView(TemplateView):
    model = Address
    form_class = AddressCreationForm
    template_name = 'address.html'

    def get_context_data(self, **kwargs):
        context = super(CreateAdressView, self).get_context_data(**kwargs)
        context['form'] = AddressCreationForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = context['form']
        if form.is_valid():
            user = self.request.user
            form.user = user.pk
            form.save()
            return redirect(reverse_lazy('accounts:login'))
        return redirect(reverse_lazy('address:new'))

new = CreateAdressView.as_view()
