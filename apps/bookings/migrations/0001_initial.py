# Generated by Django 4.2.2 on 2023-06-14 19:20

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
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('deleted', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('photo', models.ImageField(upload_to='bookings/images/')),
                ('services', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('deleted', models.DateField(auto_now=True)),
                ('number', models.CharField(max_length=50, unique=True)),
                ('capacity', models.PositiveIntegerField()),
                ('price_day', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('description', models.TextField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.hotel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('deleted', models.DateField(auto_now=True)),
                ('content', models.TextField()),
                ('score', models.FloatField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.hotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('deleted', models.DateField(auto_now=True)),
                ('start_booking', models.DateTimeField()),
                ('end_booking', models.DateTimeField()),
                ('number_guests', models.PositiveIntegerField()),
                ('status_booking', models.CharField(choices=[('C', 'confirmed'), ('P', 'pending'), ('R', 'rejected'), ('IP', 'inprogress')], max_length=2)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
