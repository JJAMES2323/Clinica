# Generated by Django 4.2.5 on 2023-09-16 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Personas",
            fields=[
                ("cedula", models.IntegerField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=30)),
                ("fecha", models.DateField()),
            ],
        ),
    ]