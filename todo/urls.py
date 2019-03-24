from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view_task/<task_id>', views.viewTask, name='view_task'),
    path('save_task', views.saveTask, name="save_task"),
    #path('complete/<task_id>', views.completeTodo, name='complete'),
    #path('delete_complete', views.deleteCompleted, name='deletecomplete'),
    #path('delete_all', views.deleteAll, name='delete_all'),
    #path('form', views.form, name='form'),


]
