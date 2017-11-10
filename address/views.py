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
        context['form_address'] = AddressCreationForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = context['form_address']
        if form.is_valid():
            address = form.save(commit=False)
            address.user = self.request.user
            user = self.request.user
            address.save()
        return redirect(reverse_lazy('accounts:profile', kwargs={'pk':user.pk}))

new = CreateAdressView.as_view()
