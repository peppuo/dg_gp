from django.urls import path

from . import views


urlpatterns = [
    path('', views.render_base, name='home'),
    path('task-logs/', views.render_logs, name='render_logs'),
    path('template-form/<int:pk>', views.render_template,
         name='practice_form_template'),
]
