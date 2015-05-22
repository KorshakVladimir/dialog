# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='depth',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
