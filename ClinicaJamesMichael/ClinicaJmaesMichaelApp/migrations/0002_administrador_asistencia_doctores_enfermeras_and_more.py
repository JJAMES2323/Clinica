# Generated by Django 4.2.5 on 2023-10-01 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ClinicaJmaesMichaelApp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="administrador",
            fields=[
                (
                    "cedula",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="ClinicaJmaesMichaelApp.personas",
                    ),
                ),
                ("nombre", models.CharField(max_length=30, null=True)),
                ("rol", models.CharField(max_length=30, null=True)),
                ("usuario", models.CharField(max_length=30, null=True)),
                ("password", models.CharField(max_length=30, null=True)),
                ("correoE", models.EmailField(max_length=30, null=True)),
                ("telefono", models.IntegerField(null=True)),
                ("direccion", models.CharField(max_length=30, null=True)),
                ("fecha", models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Asistencia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                        default=1
                    ),
                ),
                ("fecha", models.DateTimeField(null=True)),
                ("usuario", models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="doctores",
            fields=[
                (
                    "cedula",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="ClinicaJmaesMichaelApp.personas",
                    ),
                ),
                ("nombre", models.CharField(max_length=30, null=True)),
                ("rol", models.CharField(max_length=30, null=True)),
                ("usuario", models.CharField(max_length=30, null=True)),
                ("password", models.CharField(max_length=30, null=True)),
                ("correoE", models.EmailField(max_length=30, null=True)),
                ("telefono", models.IntegerField(null=True)),
                ("direccion", models.CharField(max_length=30, null=True)),
                ("fecha", models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Enfermeras",
            fields=[
                (
                    "cedula",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="ClinicaJmaesMichaelApp.personas",
                    ),
                ),
                ("nombre", models.CharField(max_length=30, null=True)),
                ("rol", models.CharField(max_length=30, null=True)),
                ("usuario", models.CharField(max_length=30, null=True)),
                ("password", models.CharField(max_length=30, null=True)),
                ("correoE", models.EmailField(max_length=30, null=True)),
                ("telefono", models.IntegerField(null=True)),
                ("direccion", models.CharField(max_length=30, null=True)),
                ("fecha", models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="nuevosDatos",
            fields=[
                (
                    "cedula",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="ClinicaJmaesMichaelApp.personas",
                    ),
                ),
                ("nombre", models.CharField(max_length=30, null=True)),
                ("rol", models.CharField(max_length=30, null=True)),
                ("usuario", models.CharField(max_length=30, null=True)),
                ("password", models.CharField(max_length=30, null=True)),
                ("correoE", models.EmailField(max_length=30, null=True)),
                ("telefono", models.IntegerField(null=True)),
                ("direccion", models.CharField(max_length=30, null=True)),
                ("fecha", models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Ordenes",
            fields=[
                (
                    "orden",
                    models.IntegerField(
                        max_length=30, primary_key=True, serialize=False
                    ),
                ),
                ("cedulaPcaiente", models.IntegerField(null=True)),
                ("fecha", models.DateField(null=True)),
                ("cedulaMedico", models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Paciente",
            fields=[
                ("nombre", models.CharField(max_length=30, null=True)),
                ("cedula", models.IntegerField(primary_key=True, serialize=False)),
                ("fecha", models.DateField(null=True)),
                ("genero", models.CharField(max_length=10, null=True)),
                ("direccion", models.CharField(max_length=30, null=True)),
                ("telefono", models.IntegerField(null=True)),
                ("correoE", models.EmailField(max_length=30, null=True)),
                ("nombreContacto", models.CharField(max_length=30, null=True)),
                ("parentezcoContacto", models.CharField(max_length=30, null=True)),
                ("telefonoContacto", models.IntegerField(null=True)),
                ("nombreSeguro", models.CharField(max_length=30, null=True)),
                ("numeroPoliza", models.IntegerField(null=True)),
                ("estadoPoliza", models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="recurososHumanos",
            fields=[
                (
                    "cedula",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="ClinicaJmaesMichaelApp.personas",
                    ),
                ),
                ("nombre", models.CharField(max_length=30, null=True)),
                ("rol", models.CharField(max_length=30, null=True)),
                ("usuario", models.CharField(max_length=30, null=True)),
                ("password", models.CharField(max_length=30, null=True)),
                ("correoE", models.EmailField(max_length=30, null=True)),
                ("telefono", models.IntegerField(null=True)),
                ("direccion", models.CharField(max_length=30, null=True)),
                ("fecha", models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Soporte",
            fields=[
                (
                    "cedula",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="ClinicaJmaesMichaelApp.personas",
                    ),
                ),
                ("nombre", models.CharField(max_length=30, null=True)),
                ("rol", models.CharField(max_length=30, null=True)),
                ("usuario", models.CharField(max_length=30, null=True)),
                ("password", models.CharField(max_length=30, null=True)),
                ("correoE", models.EmailField(max_length=30, null=True)),
                ("telefono", models.IntegerField(null=True)),
                ("direccion", models.CharField(max_length=30, null=True)),
                ("fecha", models.DateField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name="personas",
            name="correoE",
            field=models.EmailField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="personas",
            name="direccion",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="personas",
            name="password",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="personas",
            name="rol",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="personas",
            name="telefono",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="personas",
            name="usuario",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="personas",
            name="fecha",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="personas",
            name="nombre",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.CreateModel(
            name="AyudaDiagnostica",
            fields=[
                (
                    "ordenAyud",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="ClinicaJmaesMichaelApp.ordenes",
                    ),
                ),
                ("nmbreAyuda", models.CharField(max_length=30, null=True)),
                ("cantidad", models.CharField(max_length=30, null=True)),
                ("especialista", models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="HistoriaClinica",
            fields=[
                (
                    "cedulaPcaiente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="ClinicaJmaesMichaelApp.paciente",
                    ),
                ),
                ("fecha", models.DateField(null=True)),
                ("cedulaMedico", models.IntegerField(null=True)),
                ("MotivoCosnulta", models.CharField(max_length=100, null=True)),
                ("sintamotologia", models.CharField(max_length=100, null=True)),
                ("diagnostico", models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Medicamentos",
            fields=[
                (
                    "ordenMed",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="ClinicaJmaesMichaelApp.ordenes",
                    ),
                ),
                ("nmbreMedicamento", models.CharField(max_length=30, null=True)),
                ("dosis", models.CharField(max_length=30, null=True)),
                ("duracionTratamiento", models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Procedimiento",
            fields=[
                (
                    "ordenProc",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="ClinicaJmaesMichaelApp.ordenes",
                    ),
                ),
                ("nmbreProcedimiento", models.CharField(max_length=30, null=True)),
                ("cantidad", models.CharField(max_length=30, null=True)),
                ("frecuencia", models.CharField(max_length=30, null=True)),
                ("especialista", models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Vista",
            fields=[
                (
                    "cedulaPcaiente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="ClinicaJmaesMichaelApp.paciente",
                    ),
                ),
                ("fecha", models.DateField(null=True)),
                ("cedulaMedico", models.IntegerField(null=True)),
                ("presion", models.CharField(max_length=30, null=True)),
                ("temperatura", models.CharField(max_length=30, null=True)),
                ("pulso", models.CharField(max_length=30, null=True)),
                ("oxigeno", models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Sesion",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("token", models.CharField(default="", max_length=200, null=True)),
                (
                    "usuario",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ClinicaJmaesMichaelApp.personas",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Factura",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nombreCompañia", models.CharField(max_length=30, null=True)),
                ("numeroPoliza", models.IntegerField(null=True)),
                ("estadoPoliza", models.BooleanField(null=True)),
                (
                    "nombreMedico",
                    models.ForeignKey(
                        max_length=30,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ClinicaJmaesMichaelApp.personas",
                    ),
                ),
                (
                    "nombrePaciente",
                    models.ForeignKey(
                        max_length=30,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ClinicaJmaesMichaelApp.paciente",
                    ),
                ),
            ],
        ),
    ]