from django.db import models
from django.contrib.auth.models import User

from .types import JOB_TYPES, PROPERTY_TYPES, JOB_FREQUENCIES, DURATION_TYPES

# Create your models here.
class Tasks(models.Model):
    user_id = models.ForeignKey(
        User,
        to_field="id",
        blank=False,
        related_name="user_task",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=50, default=None)
    job_type = models.PositiveSmallIntegerField(
        choices=JOB_TYPES, blank=False, null=False
    )
    rate = models.PositiveSmallIntegerField(blank=True, default=1)

    property_type = models.PositiveSmallIntegerField(
        choices=PROPERTY_TYPES, default=0, null=False
    )
    assigned_to = models.ForeignKey(
        User, to_field="id", related_name="assigned_task", on_delete=models.PROTECT
    )

    job_frequency = models.PositiveSmallIntegerField(
        choices=JOB_FREQUENCIES, default=0, null=False
    )
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=True)
    start_time = models.TimeField(auto_now=False, auto_now_add=False, null=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False, null=False)
    visit_frequency = models.PositiveIntegerField(default=0, null=True)
    duration = models.PositiveIntegerField(default=0, null=True)
    duration_type = models.PositiveSmallIntegerField(
        choices=DURATION_TYPES, default=0, null=True
    )
    address = models.TextField(blank=False, null=False)
    sign = models.CharField(max_length=50)

    def __str__(self):
        return "id: {}\nuser_id: {}\njob_type: {}\n".format(
            str(self.id), str(self.user_id), str(self.job_type)
        )

    class Meta:
        db_table = "tasks"
        indexes = [
            models.Index(fields=["user_id",]),
        ]


class Landscape(models.Model):
    job_id = models.OneToOneField(
        Tasks, to_field="id", primary_key=True, null=False, on_delete=models.CASCADE
    )
    office = models.CharField(max_length=100)
    home = models.CharField(max_length=100)
    cell = models.CharField(max_length=14)
    email = models.EmailField(null=False)
    submitted_to = models.CharField(max_length=50)
    date = models.DateField(null=False)
    subtotal = models.FloatField(null=False)
    tax = models.FloatField(null=False)
    total_contracts = models.FloatField(null=False)
    sum_of = models.FloatField(null=False)
    final_payment = models.FloatField(null=False)

    class Meta:
        db_table = "landscape"


class LandscapeFields(models.Model):
    job_id = models.ForeignKey(Landscape, to_field="job_id", on_delete=models.CASCADE)
    item = models.CharField(max_length=50, null=False)
    size = models.CharField(max_length=10, null=False)
    total = models.FloatField(null=False)

    class Meta:
        db_table = "landscape_fields"
        indexes = [
            models.Index(fields=["job_id",]),
        ]
