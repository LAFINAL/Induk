from django.contrib import admin

from .models import Board, Report, ReportComment

from Induk.admin import ArticleAdmin, BoardAdmin

admin.site.register(Board, BoardAdmin)
admin.site.register(Report, ArticleAdmin)
admin.site.register(ReportComment)
