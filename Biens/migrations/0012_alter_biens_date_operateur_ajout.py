# Generated by Django 5.1.4 on 2025-03-23 00:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biens', '0011_alter_biens_date_operateur_supprimer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biens',
            name='date_operateur_ajout',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
