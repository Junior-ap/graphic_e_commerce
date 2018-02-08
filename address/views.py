from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .models import Address
from .forms import AddressCreationForm


class CreateAddressView(TemplateView):
    model = Address
    form_class = AddressCreationForm
    template_name = 'dashboard/address.html'

    def get_context_data(self, **kwargs):
        context = super(CreateAddressView, self).get_context_data(**kwargs)
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
        return redirect(reverse_lazy('accounts:profile'))

class DeleteAddressView(TemplateView):

    def get(self, request, pk):
        address = Address.objects.get(pk=pk)
        address.delete()
        return redirect(reverse_lazy('accounts:profile'))

new = CreateAddressView.as_view()
delete = DeleteAddressView.as_view()
