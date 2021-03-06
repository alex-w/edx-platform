# Generated by Django 1.11.28 on 2020-02-14 21:30


import django_mysql.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth_dispatch', '0007_restore_application_id_constraints'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationaccess',
            name='filters',
            field=django_mysql.models.ListCharField(models.CharField(max_length=32), blank=True, help_text='Comma-separated list of filters that this application will be allowed to request.', max_length=825, null=True, size=25),
        ),
    ]
