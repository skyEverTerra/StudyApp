# Generated by Django 4.2.5 on 2024-04-09 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_calif_materia_alter_calif_alumno"),
    ]

    operations = [
        migrations.AlterField(
            model_name="calif",
            name="materia",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.materia",
            ),
        ),
    ]
