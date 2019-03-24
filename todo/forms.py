from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
  class Meta:
      model = Task
      fields = [
        'text',
        'status',
        'priority',
        'category',
        'assignee',
        'occurence',
        'occurence_desc',
        'percent_complete',
        'time_estimate_val',
        'time_estimate_metric',
        'time_actual_val',
        'time_actual_metric',
        'location',
        'due_date',


        ]
      widgets = {
        'text' : forms.TextInput(
          attrs = {'class' : 'form-control', 'placeholder': 'enter todo item', 'aria-label': 'Todo', 'aria-describedby': 'add-btn' }
        ),
        'due_date' : forms.SelectDateWidget()
      }

      '''
        status = models.CharField(max_length=3, choices=STATUSES, default='N')
  due_date = models.DateField(null=True)
  parent_id = models.IntegerField(null=True)
  prereq_id = models.IntegerField(null=True)
  category = models.CharField(max_length=1, choices=CATEGORIES, null=True)
  create_ts = models.DateTimeField(auto_now=True)
  complete_ts = models.DateTimeField(null=True)
  assignee = models.CharField(max_length=3, choices=ASSIGNEES, null=True)
  occurence = models.CharField(max_length=3, choices=OCCURRENCES, null=True)
  occurence_desc = models.CharField(max_length=16, null=True)
  priority = models.CharField(max_length=3, choices=PRIORITY, null=True)
  percent_complete = models.FloatField(null=True)
  time_estimate_val = models.FloatField(null=True)
  time_estimate_metric = models.CharField(max_length=3, choices=DURATIONS, null=True)
  time_actual_val = models.FloatField(null=True)
  time_actual_metric = models.CharField(max_length=3, choices=DURATIONS, null=True)
  location = models.CharField(max_length=64, null=True)
  '''