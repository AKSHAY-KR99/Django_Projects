from django.shortcuts import redirect


def amdin_only(func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_superuser:
            return redirect("superuser")
        else:
            return func(request,*args,**kwargs)

    return wrapper


def user_authenticated(func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("loginrequired")
        else:
            return func(request, *args,**kwargs)

    return wrapper

def no_amdin(func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_superuser:
            return redirect("no-su")
        else:
            return func(request,*args,**kwargs)

    return wrapper