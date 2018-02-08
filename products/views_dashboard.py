from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, ListView, DetailView, View, UpdateView

import cloudinary
import cloudinary.uploader
import cloudinary.api

from categories.models import Category
from accounts.polices import IsRootOrAdm, IsSalesMan

from .forms import ProductCreationForm
from .models import Product, GalleryProducts

#Metodos de Product
class CreateProductView(LoginRequiredMixin, IsRootOrAdm, CreateView):
    model = Product
    form_class = ProductCreationForm
    template_name = 'create_products_dashboard.html'
    success_url = reverse_lazy('products:list_product')


class ListProductView(LoginRequiredMixin, IsSalesMan, ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'dashboard/list_product.html'
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

class DetailProductView(LoginRequiredMixin, IsSalesMan, DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'dashboard/detail_product.html'

    def get_context_data(self, **kwargs):
        context = super(DetailProductView, self).get_context_data(**kwargs)
        context['form'] = ProductCreationForm(self.request.POST or None, instance=context['product'])
        context['gallery'] = GalleryProducts.objects.filter(product=self.kwargs['pk'], status=0)

        context['pk'] = self.kwargs['pk']
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        form = context['form']
        if form.is_valid():
            form.save()
        return redirect(reverse_lazy('products:detail_product', kwargs={'pk':self.get_object().pk}))

#Metodos de Gallery Products
class UploadImg(LoginRequiredMixin, IsRootOrAdm, View):
    model = GalleryProducts
    template_name = 'detail_product_dashboard.html'

    def post(self, request, *args, **kwargs):
        product = Product.objects.get(pk=self.kwargs['pk'])
        filep = self.request.FILES['proImg']
        contActive = GalleryProducts.objects.filter(product=product.pk, status=0).count()
        contDesabled = GalleryProducts.objects.filter(product=product.pk, status=1).count()
        if contDesabled > 0:
            gallery = GalleryProducts.objects.filter(product=product.pk, status=1)[0]
            filep.name = str(product.name) +'-'+ str(gallery.number)
            proImg = cloudinary.uploader.upload(filep, folder='Products' ,public_id=filep.name)
            gallery.img=proImg['secure_url']
            gallery.status = 0
            gallery.save()
        else:
            if contActive > 1:
                msg = 'Limite de imagens 3'
                print(msg)
            else:
                if product.imgDefault == 'none':
                    filep.name = str(product.name) +'-'+ str(contActive + 1)
                    proImg = cloudinary.uploader.upload(filep, folder='Products' ,public_id=filep.name)
                    product.imgDefault=proImg['secure_url']
                    product.save()
                else:
                    filep.name = str(product.name) +'-'+ str(contActive + 2)
                    proImg = cloudinary.uploader.upload(filep, folder='Products' ,public_id=filep.name)
                    GalleryProducts.objects.create(product=product, status=0, img=proImg['secure_url'], number=contActive + 2)
        return redirect(reverse_lazy('products:galeria-imagens', kwargs={'pk':product.pk}))

class GalleryProductsView(LoginRequiredMixin, IsRootOrAdm, TemplateView):
    model = GalleryProducts
    template_name = 'dashboard/gallery_product.html'

    def get_context_data(self, **kwargs):
        context = super(GalleryProductsView, self).get_context_data(**kwargs)
        context['gallery'] = GalleryProducts.objects.filter(product=self.kwargs['pk'], status=0)
        context['product'] = Product.objects.get(pk=self.kwargs['pk'])
        return context

class GalleryImgDeleteView(LoginRequiredMixin, IsRootOrAdm, View):

    def get(self, request, pk):
        imgProd = GalleryProducts.objects.get(pk=pk)
        pk = imgProd.product_id
        imgProd.status=1
        imgProd.save()
        return redirect(reverse_lazy('products:galeria-imagens', kwargs={'pk':pk}))

class GalleryImgDefaltView(LoginRequiredMixin, IsRootOrAdm, View):

    def get(self, request, pk):
        imgProd = GalleryProducts.objects.get(pk=pk)
        pk = imgProd.product_id
        product = Product.objects.get(pk=pk)
        imgUrl = product.imgDefault
        product.imgDefault = imgProd.img
        imgProd.img = imgUrl
        product.save()
        imgProd.save()
        return redirect(reverse_lazy('products:galeria-imagens', kwargs={'pk':pk}))


#Urls de Gallery Products
gallery_product_view = GalleryProductsView.as_view()
upload_img_product_view = UploadImg.as_view()
gallery_img_delete_view = GalleryImgDeleteView.as_view()
gallery_img_defalt_view = GalleryImgDefaltView.as_view()

#Urls de Product
create_product_view = CreateProductView.as_view()
list_product_view = ListProductView.as_view()
detail_product_view = DetailProductView.as_view()
