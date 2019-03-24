from django.contrib import admin

from .models import Task


def cancel_task(modeladmin, request, queryset):
    queryset.update(status='CAN')
cancel_task.short_description = "Cancel Selected Tasks"

def complete_task(modeladmin, request, queryset):
    queryset.update(status='COM')
complete_task.short_description = "Complete Selected Tasks"

class TaskAdmin(admin.ModelAdmin):
    list_display = ['text', 'status', 'due_date', 'priority', 'category', 'occurence']
    actions = [cancel_task, complete_task]
    date_hierarchy = 'create_ts'
    #exclude = ('orig_text',)
    fields = ('text', ('status', 'category', 'due_date', 'priority', 'assignee'), ('parent_id', 'prereq_id'), ('occurence', 'occurence_desc'),
      ('time_estimate_val', 'time_estimate_metric', 'time_actual_val', 'time_actual_metric'), ('location', 'percent_complete'))
    list_editable = ('status', 'category', 'due_date', 'priority', 'occurence')
    list_filter = ('status', 'category', 'priority', 'assignee', 'occurence_desc')
    list_per_page = 1000
    preserve_filters = True
    save_on_top = True
    search_fields = ['text', 'orig_text']


admin.site.register(Task, TaskAdmin)
