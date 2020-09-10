from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache


@never_cache
def home(request):
    if request.user.is_authenticated:
        return redirect("/create_bid/")
    return redirect("/accounts/login/")