# Generated by Django 5.0.3 on 2024-04-02 06:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_alter_task_creation_date_alter_task_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 2, 8, 17, 14, 579470), verbose_name='creation date'),
        ),
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 2, 8, 17, 14, 579482), verbose_name='end date'),
        ),
    ]
