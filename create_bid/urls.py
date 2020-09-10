from django.urls import path, include
from . import views

urlpatterns = [
    path("create_bid/", views.create_bid, name="login"),
]
