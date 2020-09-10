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


@transaction.atomic
def create_bid(request):
    return HttpResponse("hello world")