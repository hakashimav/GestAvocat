# Generated by Django 5.0.6 on 2024-09-10 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0023_evodossier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evodossier',
            name='NumAvocat',
        ),
        migrations.RemoveField(
            model_name='evodossier',
            name='Numclient',
        ),
    ]
