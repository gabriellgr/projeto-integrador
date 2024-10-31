# Generated by Django 5.1.2 on 2024-10-30 22:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cadastro", "0007_medico_is_active_paciente_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="medico",
            name="cpf",
            field=models.CharField(blank=True, max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name="medico",
            name="data_de_nascimento",
            field=models.DateField(
                default=django.utils.timezone.now, help_text="eg. 2024-10-30"
            ),
        ),
        migrations.AlterField(
            model_name="paciente",
            name="data_de_nascimento",
            field=models.DateField(
                default=django.utils.timezone.now, help_text="eg. 2024-10-30"
            ),
        ),
    ]