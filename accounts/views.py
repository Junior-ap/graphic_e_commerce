from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, ListView, DetailView, View
from .forms import UserCreationForm
from .models import User
from address.models import Address


class CreateUserView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('accounts:login')

class ListUserView(LoginRequiredMixin,ListView):
    model = User
    context_object_name = 'users'
    template_name = 'list_users_dashboard.html'
    paginate_by = 12

    def get_queryset(self):
        filtro = self.request.GET.get('filtro')
        if filtro == 'adm':
            queryset = User.objects.filter(nivel=1)
        elif filtro == 'vendedor':
            queryset = User.objects.filter(nivel=2)
        elif filtro == 'cliente':
            queryset = User.objects.filter(nivel=3)
        else:
            queryset = User.objects.all()
        return queryset

class DetailUserTaxedView(LoginRequiredMixin, TemplateView):
    template_name = 'detail_user_cadastrado.html'

    def get_context_data(self, **kwargs):
        context = super(DetailUserTaxedView, self).get_context_data(**kwargs)
        pk = kwargs['pk']
        user = get_object_or_404(User, pk=pk)
        context['user_taxed'] = user
        context['form'] = UserCreationForm(self.request.POST or None, instance=user)
        context['address'] = Address.objects.filter(pk=pk)
        return context

class ChangeStatusUserView(LoginRequiredMixin, View):
    status = 0
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.status = self.status
        user.save()
        return redirect(reverse_lazy('accounts:detail_user_cadastrado', kwargs={'pk':user.pk}))

class ChangeNivelUserView(LoginRequiredMixin, View):
    nivel = 3
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.nivel = self.nivel
        user.save()
        return redirect(reverse_lazy('accounts:detail_user_cadastrado', kwargs={'pk':user.pk}))

class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    context_object_name = 'user_taxed'
    template_name = 'profile_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['form'] = UserCreationForm(self.request.POST or None, instance=context['user_taxed'])
        return context

    def get_object(self):
        return self.request.user

#Modificar_User_Taxed
create_user = CreateUserView.as_view()
list_user = ListUserView.as_view()
detail_user_taxed = DetailUserTaxedView.as_view()
#Status_User_Taxed
active = ChangeStatusUserView.as_view()
disable = ChangeStatusUserView.as_view(status=1)
block = ChangeStatusUserView.as_view(status=2)
#Nivel_User_Taxed
adm = ChangeNivelUserView.as_view(nivel=1)
salesman = ChangeNivelUserView.as_view(nivel=2)
customer = ChangeNivelUserView.as_view()
#Modificar_User_logado
profile = ProfileView.as_view()
