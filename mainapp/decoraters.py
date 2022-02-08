from django.http import HttpResponse
from django.shortcuts import render, redirect

def allowed_users(allowed=[]):
    def decorater(view_func):
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed:
                return view_func(request, *args, **kwargs)
            else:
                return redirect("dashboard-client")
        return wrapper
    return decorater