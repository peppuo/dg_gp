from django.urls import path

from . import views


urlpatterns = [
    path('', views.render_base, name='home'),
    path('tasks-table/', views.render_tasks_table, name='task_table'),
    # path('task-logs/', views.get_logs, name='get_logs'),
    # path('insert-log/', views.insert_log, name='insert_log'),
    # path('edit-log/<int:pk>', views.edit_log, name='edit_log'),
    # path('edit-user/<int:pk>', views.edit_user,
    #      name='edit_user'),
]
