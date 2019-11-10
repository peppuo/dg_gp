from django.contrib import admin

from .models import UserInfo, Department, Email

admin.site.register(UserInfo)
admin.site.register(Department)
admin.site.register(Email)