# Generated by Django 4.2.18 on 2025-01-15 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0003_alter_reservamodel_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservamodel',
            name='sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='reservas.salamodel'),
        ),
    ]
