# Generated by Django 2.0 on 2018-03-23 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='credential',
            field=models.CharField(blank=True, choices=[('A', 'Athlete'), ('T', 'Team'), ('R', 'Referee'), ('L', 'League Organizer'), ('Admin', 'ADMIN')], max_length=200, null=True, verbose_name='Credential'),
        ),
    ]
