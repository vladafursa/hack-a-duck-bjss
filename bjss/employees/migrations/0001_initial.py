# Generated by Django 5.1.2 on 2024-11-01 20:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employees",
            fields=[
                (
                    "name",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "skills",
                    models.TextField(help_text="List of skills, separated by commas."),
                ),
                (
                    "experience",
                    models.PositiveIntegerField(help_text="Years of experience"),
                ),
                ("location", models.CharField(max_length=100)),
                ("type_of_work", models.CharField(max_length=50)),
                (
                    "availability",
                    models.DateField(
                        help_text="Date the candidate is available to start"
                    ),
                ),
                ("security_clearance", models.CharField(max_length=50)),
                (
                    "temperament",
                    models.CharField(
                        choices=[
                            ("melancholic", "Melancholic"),
                            ("choleric", "Choleric"),
                            ("sanguine", "Sanguine"),
                            ("phlegmatic", "Phlegmatic"),
                        ],
                        help_text="Select the candidate's temperament",
                        max_length=50,
                    ),
                ),
            ],
            options={
                "verbose_name": "Participant",
                "verbose_name_plural": "Participants",
            },
        ),
    ]