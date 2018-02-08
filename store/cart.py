from django.shortcuts import render, redirect
from .models import Order

class AddCart():
    def dispatch(self, request, *args, **kwargs):
        us = self.request.user
        ordem = Order.objects.filter(user=us.pk , status=0)
        if not ordem:
            Order.objects.create(user=us)
        return super(AddCart, self).dispatch(request, *args, **kwargs)
