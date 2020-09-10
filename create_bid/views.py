from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import transaction

from .forms import CreateBidForm
from .models import Tasks, Landscape


@transaction.atomic
@login_required
def create_bid(request):
    form = CreateBidForm(request.POST or None)
    if form.is_valid():
        user_id = request.user
        title = form.cleaned_data.get("title")
        job_type = form.cleaned_data.get("job_type")
        rate = form.cleaned_data.get("rate")
        property_type = form.cleaned_data.get("property_type")
        job_frequency = form.cleaned_data.get("job_frequency")
        start_date = form.cleaned_data.get("start_date")
        end_date = form.cleaned_data.get("end_date")
        start_time = form.cleaned_data.get("start_time")
        end_time = form.cleaned_data.get("end_time")
        visit_frequency = form.cleaned_data.get("visit_frequency")
        duration = form.cleaned_data.get("duration")
        duration_type = form.cleaned_data.get("duration_type")
        address = form.cleaned_data.get("address")
        sign = form.cleaned_data.get("sign")
        assigend_to = request.user.id

        office = form.cleaned_data.get("office")
        home = form.cleaned_data.get("home")
        cell = form.cleaned_data.get("cell")
        email = form.cleaned_data.get("email")
        submitted_to = form.cleaned_data.get("submitted_to")
        date = form.cleaned_data.get("date")
        sub_total = form.cleaned_data.get("sub_total")
        tax = form.cleaned_data.get("tax")
        total_contracts = form.cleaned_data.get("total_contracts")
        sum_of = form.cleaned_data.get("sum_of")
        final_payment = form.cleaned_data.get("final_payment")

        fields = {
            "user_id": user_id,
            "title": title,
            "job_type": job_type,
            "rate": rate,
            "property_type": property_type,
            "job_frequency": job_frequency,
            "start_date": start_date,
            "end_date": end_date,
            "start_time": start_time,
            "end_time": end_time,
            "visit_frequency": visit_frequency,
            "duration": duration,
            "duration_type": duration_type,
            "address": address,
            "sign": sign,
            "assigned_to_id": assigend_to,
        }
        tasks = Tasks(**fields)
        tasks.save()
        landscape_fields = {
            "job_id": tasks,
            "office": office,
            "home": home,
            "cell": cell,
            "email": email,
            "submitted_to": submitted_to,
            "date": date,
            "subtotal": sub_total,
            "tax": tax,
            "total_contracts": total_contracts,
            "sum_of": sum_of,
            "final_payment": final_payment,
        }
        landscape = Landscape(**landscape_fields)
        landscape.save()
        return redirect("/create_bid/")
    return render(
        request, "crispy_form.html", {"form": form, "form_title": "Create Bid"},
    )
