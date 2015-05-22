
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Answer(models.Model):
    text_answer = models.CharField(max_length=200, verbose_name='Текст ответа')
    depth = models.IntegerField(default=0)

    def __unicode__(self):
        return self.text_answer


class Questions(models.Model):
    text_questions = models.CharField(
        max_length=200, verbose_name='Текст Вопроса')
    relation_answer = models.ForeignKey(Answer)
    point_answer = models.IntegerField(default=0, verbose_name='Очки ответа')
    question_answer = models.IntegerField(default=0)

    def __unicode__(self):
        return self.text_questions


class User_rezult(models.Model):
    user_output = User
    question_output = Questions
    answer_output = Answer
    sessio_output = models.IntegerField(default=0)
