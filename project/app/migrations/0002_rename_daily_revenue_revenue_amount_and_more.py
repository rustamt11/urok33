# Generated by Django 4.2.6 on 2023-10-23 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='revenue',
            old_name='daily_revenue',
            new_name='amount',
        ),
        migrations.RemoveField(
            model_name='revenue',
            name='monthly_revenue',
        ),
        migrations.RemoveField(
            model_name='revenue',
            name='weekly_revenue',
        ),
    ]
