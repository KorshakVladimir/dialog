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
                ('text_answer', models.CharField(max_length=200)),
                ('point_answer', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text_questions', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User_rezult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sessio_output', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='relation_answer',
            field=models.ForeignKey(to='tree.Questions'),
        ),
    ]
