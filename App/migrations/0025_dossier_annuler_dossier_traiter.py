# Generated by Django 5.0.6 on 2024-09-10 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0024_remove_evodossier_numavocat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dossier',
            name='annuler',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dossier',
            name='traiter',
            field=models.BooleanField(default=False),
        ),
    ]
