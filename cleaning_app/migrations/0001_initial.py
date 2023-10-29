# Generated by Django 4.1.7 on 2023-10-14 13:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('complaint_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('roll_number', models.CharField(max_length=10)),
                ('name_of_student', models.CharField(max_length=100)),
                ('complaint', models.TextField()),
                ('date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('worker_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('worker_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cleaning',
            fields=[
                ('cleaning_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('roll_number', models.CharField(max_length=10)),
                ('name_of_student', models.CharField(max_length=100)),
                ('hostel', models.CharField(max_length=50)),
                ('room_number', models.CharField(max_length=10)),
                ('cleaning_task', models.CharField(choices=[('Room', 'Room'), ('Washroom', 'Washroom'), ('Corridor', 'Corridor')], max_length=10)),
                ('date_time', models.DateTimeField()),
                ('worker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cleaning_app.worker')),
            ],
        ),
    ]