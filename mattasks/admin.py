from django.contrib import admin
from .models import Category, Status, Importance, Tasks

admin.site.register(Category)
admin.site.register(Status)
admin.site.register(Importance)
admin.site.register(Tasks)
