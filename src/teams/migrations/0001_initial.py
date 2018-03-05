# Generated by Django 2.0 on 2018-03-05 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leagues', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('abbrev', models.CharField(blank=True, max_length=4, null=True)),
                ('bio', models.CharField(blank=True, max_length=125, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('league_instance', models.ManyToManyField(blank=True, related_name='teams', to='leagues.League')),
            ],
        ),
        migrations.CreateModel(
            name='TeamOwnerPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(max_length=20)),
            ],
        ),
    ]
