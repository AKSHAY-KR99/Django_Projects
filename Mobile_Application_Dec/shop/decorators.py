from django.shortcuts import redirect


def admin_permission_required(func):
    def wrapper(request):
        if not request.user.is_superuser:
            return redirect("error")
        else:
            return func(request)
    return wrapper

def admin_permission_required_id(func):
    def wrapper(request,id):
        if not request.user.is_superuser:
            return redirect("error")
        else:
            return func(request,id)
    return wrapper

def login_authentication(func):
    def wrapper(request):
        if not request.user.is_authenticated:
            return redirect("userlogin")
        else:
            return func(request)
    return wrapper


def login_authentication_id(func):
    def wrapper(request,id):
        if not request.user.is_authenticated:
            return redirect("userlogin")
        else:
            return func(request,id)
    return wrapper