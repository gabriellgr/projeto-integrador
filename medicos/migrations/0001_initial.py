# Generated by Django 5.1.1 on 2024-10-09 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicos',
            fields=[
                ('id_medico', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('telefone', models.TextField(max_length=15)),
            ],
        ),
    ]