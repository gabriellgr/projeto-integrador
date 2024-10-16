# Generated by Django 5.1.1 on 2024-10-09 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicos',
            name='crm',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='medicos',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='medicos',
            name='especialidade',
            field=models.CharField(max_length=100, null=True),
        ),
    ]