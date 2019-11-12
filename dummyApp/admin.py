from django.contrib import admin

from .models import Category, Department, Status, Task, UserInfo

admin.site.register(Category)
admin.site.register(Department)
admin.site.register(Status)
admin.site.register(UserInfo)
admin.site.register(Task)
