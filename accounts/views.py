from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, CreateView, ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from address.models import Address
from django.core.urlresolvers import reverse_lazy
from .forms import UserCreationForm


class CreateSalesmanView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('accounts:login')

class ListUserView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'list_users.html'
    paginate_by = 20

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

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'


class ProfileView(DetailView):
    model = User
    context_object_name = 'user_request'
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['form'] = UserUpdateForm(self.request.POST or None, instance=context['user_request'])
        return context

    def get_object(self):
        return self.request.user

class DetailUserView(TemplateView):
    template_name = 'detail_user.html'

    def get_context_data(self, **kwargs):
        context = super(DetailUserView, self).get_context_data(**kwargs)
        pk = kwargs['pk']
        user = get_object_or_404(User, pk=pk)
        context['user'] = user
        context['form'] = UserCreationForm(self.request.POST or None, instance=user)
        context['address'] = Address.objects.filter(pk=pk)
        return context

class ChangeStatusUserView(View):
    status = 0
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.status = self.status
        user.save()
        return redirect(reverse_lazy('accounts:detail', kwargs={'pk':user.pk}))

class ChangeNivelUserView(View):
    nivel = 3
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.nivel = self.nivel
        user.save()
        return redirect(reverse_lazy('accounts:detail', kwargs={'pk':user.pk}))


create_user = CreateSalesmanView.as_view()
list_user = ListUserView.as_view()
detail_user = DetailUserView.as_view()
#Status_User
active = ChangeStatusUserView.as_view()
disable = ChangeStatusUserView.as_view(status=1)
block = ChangeStatusUserView.as_view(status=2)
#Nivel_User
adm = ChangeNivelUserView.as_view(nivel=1)
salesman = ChangeNivelUserView.as_view(nivel=2)
customer = ChangeNivelUserView.as_view()

#Modificar
profile = ProfileView.as_view()
dashboard = DashboardView.as_view()
