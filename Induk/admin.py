from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from accounts.forms import UserForm

admin.site.unregister(Group)
admin.site.unregister(Site)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["author", "title"]


class AccountAdmin(admin.ModelAdmin):
    form =UserForm
    list_display = ["username", "signup_approved", "is_active", "is_staff"]


class BoardAdmin(admin.ModelAdmin):
    list_display = ["title", "active"]
