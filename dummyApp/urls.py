from django.urls import path

from . import views


urlpatterns = [
    path('', views.render_base, name='home'),
    path('task-logs/', views.render_logs, name='render_logs'),
    path('insert-log/', views.render_insert_log, name='insert_log'),
    path('edit-user/<int:pk>', views.render_edit_user,
         name='edit_user'),

]
