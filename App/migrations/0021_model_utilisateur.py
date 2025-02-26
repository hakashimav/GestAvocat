# Generated by Django 5.0.6 on 2024-09-07 19:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0020_dossier_date_modification'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Model_Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=50, null=True)),
                ('postnom', models.CharField(blank=True, max_length=50, null=True)),
                ('prenom', models.CharField(blank=True, max_length=50, null=True)),
                ('sexe', models.CharField(blank=True, max_length=10, null=True)),
                ('telephone', models.CharField(blank=True, max_length=50, null=True)),
                ('date_naissance', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('adress', models.CharField(blank=True, max_length=150, null=True)),
                ('utilisateur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='utilisateur_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
