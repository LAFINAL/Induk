from django.contrib import admin
from .models import Learning, LearningComment
from Induk.admin import ArticleAdmin


admin.site.register(Learning, ArticleAdmin)
admin.site.register(LearningComment)
