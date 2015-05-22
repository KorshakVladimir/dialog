
# -*- coding: utf-8 -*-

from django.shortcuts import render
from . models import Questions, Answer


def index(request, answer_id=1):
    context = {}
    answer = Answer.objects.get(id=answer_id)

    questions = Questions.objects.filter(relation_answer_id=answer.id)
    context['answer'] = answer
    context['questions'] = questions
    return render(request, 'gameplace.html', context)
