from django.shortcuts import redirect

def amdin_only(func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_superuser:
            return redirect("error")
        else:
            return func(request,*args,**kwargs)

    return wrapper

