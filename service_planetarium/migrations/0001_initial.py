# Generated by Django 4.0.4 on 2024-12-26 16:47

from django.db import migrations, models
import django.db.models.deletion
import service_planetarium.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AstronomyShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=service_planetarium.models.astronomy_show_image_file_path)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='PlanetariumDome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rows', models.IntegerField()),
                ('seats_in_row', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ShowSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_time', models.DateTimeField()),
                ('astronomy_show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='show', to='service_planetarium.astronomyshow')),
                ('planetarium_dome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='show', to='service_planetarium.planetariumdome')),
            ],
            options={
                'ordering': ['-show_time'],
            },
        ),
        migrations.CreateModel(
            name='ShowTheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.IntegerField()),
                ('seat', models.IntegerField()),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='service_planetarium.reservation')),
                ('show_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='service_planetarium.showsession')),
            ],
            options={
                'ordering': ['row', 'seat'],
            },
        ),
    ]
