# Generated by Django 4.2.5 on 2024-04-09 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alumno_maestro"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="calif", unique_together={("alumno", "materia")},
        ),
    ]
