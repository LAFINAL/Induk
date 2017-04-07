from django.contrib import admin
from .models import Questions, QuestionsComment
from Induk.admin import ArticleAdmin

admin.site.register(Questions, ArticleAdmin)
admin.site.register(QuestionsComment)
