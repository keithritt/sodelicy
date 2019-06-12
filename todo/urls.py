from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view_task/<task_id>', views.viewTask, name='view_task'),
    path('save_task', views.saveTask, name="save_task"),
    path('util/<action>', views.util, name="util"),
    path('<filter>', views.index, name="filter"),


]
