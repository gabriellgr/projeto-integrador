# Generated by Django 5.1.3 on 2024-11-21 02:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0004_alter_medico_data_de_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='data_de_nascimento',
            field=models.DateField(default=django.utils.timezone.now, help_text='eg. 2024-11-21'),
        ),
    ]
