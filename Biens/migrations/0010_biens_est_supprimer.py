# Generated by Django 5.1.4 on 2025-03-01 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biens', '0009_biens_date_operateur_supprimer'),
    ]

    operations = [
        migrations.AddField(
            model_name='biens',
            name='est_supprimer',
            field=models.BooleanField(default=False),
        ),
    ]
