# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0002_questions_depth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='point_answer',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\x9e\xd1\x87\xd0\xba\xd0\xb8 \xd0\xbe\xd1\x82\xd0\xb2\xd0\xb5\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='text_answer',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd0\xbe\xd1\x82\xd0\xb2\xd0\xb5\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='depth',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='questions',
            name='text_questions',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd0\x92\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='user_rezult',
            name='sessio_output',
            field=models.IntegerField(default=0),
        ),
    ]
