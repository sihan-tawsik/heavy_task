from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div
from crispy_forms.bootstrap import PrependedText, FormActions

from .types import JOB_TYPES, PROPERTY_TYPES, JOB_FREQUENCIES, DURATION_TYPES
from .models import Tasks


class CreateBidForm(forms.Form):
    title = forms.CharField(label="Title")
    job_type = forms.ChoiceField(label="Job Type", choices=JOB_TYPES)
    rate = forms.DecimalField(label="Rating", max_value=5, min_value=1)
    property_type = forms.ChoiceField(label="Property Type", choices=PROPERTY_TYPES)
    job_frequency = forms.ChoiceField(label="Job Frequency", choices=JOB_FREQUENCIES)
    start_date = forms.DateField(widget=forms.SelectDateWidget)
    end_date = forms.DateField(widget =forms.SelectDateWidget)
    start_time = forms.TimeField(widget=forms.TimeInput(format="%H:%M"))
    end_time = forms.TimeField(widget=forms.TimeInput(format="%H:%M"))
    visit_frequency = forms.DecimalField(label="Visit Frequency", min_value=0)
    duration = forms.DecimalField(label="Duration", min_value=0)
    duration_type = forms.ChoiceField(choices=DURATION_TYPES)
    address = forms.CharField(label="Address")
    sign = forms.CharField(label="Authorized Sign")

    def __init__(self, *args, **kwargs):
        super(CreateBidForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.layout = Layout(
            "title",
            Row(
                Column("job_type", css_class="form-group col-md-6 mb-0"),
                Column("rate", css_class="form-group col-md-6 mb-0"),
            ),
            "property_type",
            "job_frequency",
            Row(
                Column("start_date", css_class="form-group col-md-6 mb-0"),
                Column("end_date", css_class="form-group col-md-6 mb-0"),
            ),
            Row(
                Column("start_time", css_class="form-group col-md-6 mb-0"),
                Column("end_time", css_class="form-group col-md-6 mb-0"),
            ),
            "visit_frequency",
            Row(
                Column("duration", css_class="form-group col-md-6 mb-0"),
                Column("duration_type", css_class="form-group col-md-6 mb-0"),
            ),
            "address",
            "sign",
            FormActions(
                Submit("submit", "Create bid", css_class="btn btn-block btn-lg")
            ),
        )

    def clean(self, *args, **keyargs):
        title = self.cleaned_data.get("title")
        job_type = self.cleaned_data.get("job_type")
        rate = self.cleaned_data.get("rate")
        property_type = self.cleaned_data.get("property_type")
        job_frequency = self.cleaned_data.get("job_frequency")
        start_date = self.cleaned_data.get("start_date")
        end_date = self.cleaned_data.get("end_date")
        start_time = self.cleaned_data.get("start_time")
        end_time = self.cleaned_data.get("end_time")
        visit_frequency = self.cleaned_data.get("visit_frequency")
        duration = self.cleaned_data.get("duration")
        duration_type = self.cleaned_data.get("duration_type")
        address = self.cleaned_data.get("address")
        sign = self.cleaned_data.get("sign")

        if not (title or job_type):
            raise forms.ValidationError("Cannot be empty")
        if start_time and end_time:
            if end_time < start_time:
                raise forms.ValidationError("end time can't be smaller than start time")
        if end_date:
            if end_date < start_date:
                raise forms.ValidationError("end time can't be smaller than start time")

        return super(CreateBidForm, self).clean(*args, **keyargs)
