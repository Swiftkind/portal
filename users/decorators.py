from django.shortcuts import redirect


def user_is_logged(function):

    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return function(request, *args, **kwargs)

    return wrap
