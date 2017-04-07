from django.contrib import admin
from .models import User
from Induk.admin import AccountAdmin

# admin.site.register(Profile, AccountAdmin)
admin.site.register(User, AccountAdmin)
