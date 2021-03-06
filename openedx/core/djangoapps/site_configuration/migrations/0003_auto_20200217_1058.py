# Generated by Django 1.11.28 on 2020-02-17 10:58


import collections

import jsonfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_configuration', '0002_auto_20160720_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='values',
            field=jsonfield.fields.JSONField(blank=True, dump_kwargs={'cls': jsonfield.encoder.JSONEncoder, 'separators': (',', ':')}, load_kwargs={'object_pairs_hook': collections.OrderedDict}),
        ),
        migrations.AlterField(
            model_name='siteconfigurationhistory',
            name='values',
            field=jsonfield.fields.JSONField(blank=True, dump_kwargs={'cls': jsonfield.encoder.JSONEncoder, 'separators': (',', ':')}, load_kwargs={'object_pairs_hook': collections.OrderedDict}),
        ),
    ]
