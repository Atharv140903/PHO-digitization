from django.shortcuts import redirect
from django.urls import reverse


def redirect_if_authenticated(fn):
    def check(request):
        if request.user.is_authenticated:
            return redirect(reverse('index'))
        return fn(request)

    return check
