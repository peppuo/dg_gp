from django.urls import path

from . import views


urlpatterns = [
    path('template/', views.render_template, name='render_template'),
]
