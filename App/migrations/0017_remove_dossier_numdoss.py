# Generated by Django 5.0.6 on 2024-08-15 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0016_dossier_is_ready'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dossier',
            name='NumDoss',
        ),
    ]
