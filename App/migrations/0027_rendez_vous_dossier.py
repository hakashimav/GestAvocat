# Generated by Django 5.0.6 on 2024-09-11 08:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0026_remove_paiement_numcleint_paiement_dossier'),
    ]

    operations = [
        migrations.AddField(
            model_name='rendez_vous',
            name='dossier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dossier_rdv', to='App.dossier'),
        ),
    ]
