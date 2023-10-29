# Generated by Django 4.0.1 on 2023-10-22 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleaning_app', '0003_alter_complaint_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='cleaning',
            name='task_description',
            field=models.TextField(default='Your Default Value', max_length=255),
        ),
        migrations.AlterField(
            model_name='cleaning',
            name='cleaning_task',
            field=models.CharField(choices=[('room', 'Room'), ('washroom', 'Washroom'), ('corridor', 'Corridor')], max_length=10),
        ),
        migrations.AlterField(
            model_name='cleaning',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
