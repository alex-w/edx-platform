# Generated by Django 1.11.28 on 2020-03-12 20:29


from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('schedules', '0016_remove_start_from_schedules'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalschedule',
            name='start',
        ),
    ]
