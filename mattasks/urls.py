from django.urls import path
from mattasks.views import render_mattasks


urlpatterns = [
    path('', render_mattasks, name='mattasks'),
]
