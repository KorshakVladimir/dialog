# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0003_auto_20150520_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='questions_answer',
            field=models.IntegerField(default=0),
        ),
    ]
