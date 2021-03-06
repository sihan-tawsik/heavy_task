# Generated by Django 3.0.3 on 2020-09-10 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("create_bid", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Landscape",
            fields=[
                (
                    "job_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="create_bid.Tasks",
                    ),
                ),
                ("office", models.CharField(max_length=100)),
                ("home", models.CharField(max_length=100)),
                ("cell", models.CharField(max_length=14)),
                ("email", models.EmailField(max_length=254)),
                ("submitted_to", models.CharField(max_length=50)),
                ("date", models.DateField()),
                ("subtotal", models.FloatField()),
                ("tax", models.FloatField()),
                ("total_contracts", models.FloatField()),
                ("sum_of", models.FloatField()),
                ("final_payment", models.FloatField()),
            ],
            options={"db_table": "landscape",},
        ),
    ]
