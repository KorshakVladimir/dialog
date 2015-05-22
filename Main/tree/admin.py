from django.contrib import admin

from . models import Answer, Questions


class QuestionsInline(admin.TabularInline):
    # list_display = ('text_answer','point_answer','questions_answer')
    model = Questions


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_answer')
    inlines = [
        QuestionsInline,
    ]


admin.site.register(Answer, AnswerAdmin)

# Register your models here.
