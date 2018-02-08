from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import render, redirect

class IsRootOrAdm(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not (request.user.nivel == 0 or request.user.nivel == 1):
            return redirect('store:dashboard')
        return super(IsRootOrAdm, self).dispatch(request, *args, **kwargs)

class IsSalesMan(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not (request.user.nivel == 0 or request.user.nivel == 1 or request.user.nivel == 2):
            return redirect('store:dashboard')
        return super(IsSalesMan, self).dispatch(request, *args, **kwargs)
