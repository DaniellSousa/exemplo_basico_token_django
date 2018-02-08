from django.contrib import admin
from models import *


class UserAppAdmin(admin.ModelAdmin):
    list_display = ["nome", "email_app", "senha"]
    search_fields = ["nome", "email_app", "senha"]


admin.site.register(UserApp, UserAppAdmin)