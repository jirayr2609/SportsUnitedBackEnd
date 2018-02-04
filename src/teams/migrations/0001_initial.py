# Generated by Django 2.0 on 2018-01-31 01:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('teamID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('abbrev', models.CharField(blank=True, max_length=4, null=True)),
                ('bio', models.CharField(blank=True, max_length=125, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('captain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeamAccolades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leagueID', models.IntegerField()),
                ('accolade', models.CharField(max_length=50)),
                ('teamID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.Team')),
            ],
        ),
        migrations.CreateModel(
            name='TeamOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TeamOwnerPermissions',
            fields=[
                ('permissionID', models.AutoField(primary_key=True, serialize=False)),
                ('permission', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TeamPlayers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suspended', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('teamID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.Team')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='teamowner',
            name='permission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.TeamOwnerPermissions'),
        ),
        migrations.AddField(
            model_name='teamowner',
            name='teamID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.Team'),
        ),
        migrations.AddField(
            model_name='teamowner',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
