# Generated by Django 5.1.4 on 2025-03-23 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biens', '0014_alter_biens_date_operateur_ajout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biens',
            name='date_operateur_ajout',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
