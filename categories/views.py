from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, View

from django.core.urlresolvers import reverse_lazy

from .models import Category
from .forms import CreateCategoryForm

class CreateCategoryView(CreateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = 'new_category.html'
    success_url = reverse_lazy('categories:list_categories')

class ListCategoryView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'list_category.html'
    paginate_by = 10

class DetailCategoryView(DetailView):
    model = Category
    form_class = CreateCategoryForm
    context_object_name = 'category'
    template_name = 'detail_category.html'

    def get_context_data(self, **kwargs):
        context = super(DetailCategoryView, self).get_context_data(**kwargs)
        context['form'] = CreateCategoryForm(self.request.POST or None, instance=context['category'])
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        form = context['form']
        if form.is_valid():
            form.save()
        return redirect(reverse_lazy('categories:list_categories'))


create_category = CreateCategoryView.as_view()
list_category = ListCategoryView.as_view()
detail_category = DetailCategoryView.as_view()
