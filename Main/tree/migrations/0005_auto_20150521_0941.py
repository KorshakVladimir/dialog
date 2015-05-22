# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0004_answer_questions_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='questions_answer',
            new_name='depth',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='depth',
            new_name='question_answer',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='point_answer',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='relation_answer',
        ),
        migrations.AddField(
            model_name='questions',
            name='point_answer',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\x9e\xd1\x87\xd0\xba\xd0\xb8 \xd0\xbe\xd1\x82\xd0\xb2\xd0\xb5\xd1\x82\xd0\xb0'),
        ),
        migrations.AddField(
            model_name='questions',
            name='relation_answer',
            field=models.ForeignKey(default=0, to='tree.Answer'),
            preserve_default=False,
        ),
    ]
