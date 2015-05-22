# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text_answer', models.CharField(max_length=200, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd0\xbe\xd1\x82\xd0\xb2\xd0\xb5\xd1\x82\xd0\xb0')),
                ('depth', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text_questions', models.CharField(max_length=200, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd0\x92\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xb0')),
                ('point_answer', models.IntegerField(default=0, verbose_name=b'\xd0\x9e\xd1\x87\xd0\xba\xd0\xb8 \xd0\xbe\xd1\x82\xd0\xb2\xd0\xb5\xd1\x82\xd0\xb0')),
                ('question_answer', models.IntegerField(default=0)),
                ('relation_answer', models.ForeignKey(to='tree.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='User_rezult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sessio_output', models.IntegerField(default=0)),
            ],
        ),
    ]
