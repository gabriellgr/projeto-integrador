# Generated by Django 5.1.1 on 2024-10-07 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PI_SAGe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientes',
            name='data_consulta',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='senha',
            field=models.CharField(max_length=128),
        ),
    ]
