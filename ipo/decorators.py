from django.http import HttpResponse
from django.shortcuts import redirect


#view_func is login page here
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

# this allows only the authorized users to get in to the admin page and restrict all others

# def allowed_users(allowed_roles=[]):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):
#             group = None
#             if request.user.groups.exists():
#                 group = request.user.groups.all()[0].name
#
#                 if group in allowed_roles:
#                     return view_func(request, *args, **kwargs)
#                 else:
#                     return HttpResponse('not Authorized')
#         return wrapper_func
#     return decorator
#
#
# from django.http import HttpResponse


