# Generated by Django 5.0.6 on 2024-08-11 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_alter_client_faxclient_alter_client_numclien_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='FaxClient',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='NumCleint',
            field=models.IntegerField(auto_created=True, blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='NumClien',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='Numrccm',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
