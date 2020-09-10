from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import (
    HttpResponseRedirect,
    Http404,
    HttpResponse,
)
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.core.exceptions import DisallowedRedirect
from django.db import transaction
from pytz import utc, timezone
from datetime import datetime, timedelta

from .forms import UsersLoginForm, UsersRegisterForm


@never_cache
def login_view(request):
    if request.user.is_authenticated:
        return redirect("/create_bid/")
    form = UsersLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/create_bid/")
    return render(
        request,
        "crispy_form.html",
        {"form": form, "form_title": "Login", "bg_image": "login.svg"},
    )


@never_cache
@transaction.atomic
def register_view(request):
    if request.user.is_authenticated:
        return redirect("/create_bid/")
    form = UsersRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        login(request, user)
        return redirect("/create_bid/")
    return render(
        request,
        "crispy_form.html",
        {"form": form, "form_title": "Register", "bg_image": "register.svg"},
    )


@never_cache
@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/accounts/login/")
