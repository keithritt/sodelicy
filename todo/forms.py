from django import forms
from .models import Task
from tempus_dominus.widgets import DatePicker#, TimePicker, DateTimePicker

class TaskForm(forms.ModelForm):
  class Meta:
      model = Task
      fields = [
        #'text',
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
        #'text' : forms.TextInput(
        #  attrs = {'class' : 'form-control', 'placeholder': 'enter todo item', 'aria-label': 'Todo', 'aria-describedby': 'add-btn' }
        #),
        'due_date' : forms.SelectDateWidget()
      }

class TaskEditForm(forms.ModelForm):
  class Meta:
      model = Task
      fields = [
        'text',
        'status',
        #'start_date',
        'due_date',
        'parent_id',
        'prereq_id',
        'priority',
        'category',
        #'create_ts',
        'complete_ts',
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
        'orig_text',
        'notes',
        #'is_template',


        ]
      widgets = {
        #'text' : forms.TextInput(
        #  attrs = {'class' : 'form-control', 'placeholder': 'enter todo item', 'aria-label': 'Todo', 'aria-describedby': 'add-btn' }
        #),
        #'due_date' : forms.SelectDateWidget()
        'due_date': DatePicker()
      }

      '''
  text = models.CharField(max_length=128)
  status = models.CharField(max_length=4, choices=STATUSES, default='NEW', blank=True)
  start_date = models.DateField(null=True, blank=True)
  due_date = models.DateField(null=True, blank=True)
  parent_id = models.IntegerField(null=True, blank=True)
  prereq_id = models.IntegerField(null=True, blank=True)
  category = models.CharField(max_length=4, choices=CATEGORIES, null=True, blank=True)
  create_ts = models.DateTimeField(auto_now=True)
  complete_ts = models.DateTimeField(null=True, blank=True)
  assignee = models.CharField(max_length=4, choices=ASSIGNEES, null=True, blank=True, default='KEI')
  occurence = models.CharField(max_length=4, choices=OCCURRENCES, null=True, blank=True, default='ONCE')
  occurence_desc = models.CharField(max_length=16, null=True, blank=True)
  priority = models.CharField(max_length=4, choices=PRIORITY, null=True, blank=True)
  percent_complete = models.FloatField(null=True, blank=True)
  time_estimate_val = models.FloatField(null=True, blank=True)
  time_estimate_metric = models.CharField(max_length=4, choices=DURATIONS, null=True, blank=True)
  time_actual_val = models.FloatField(null=True, blank=True)
  time_actual_metric = models.CharField(max_length=4, choices=DURATIONS, null=True, blank=True)
  location = models.CharField(max_length=64, null=True, blank=True)
  orig_text = models.CharField(max_length=64, null=True, blank=True)
  notes = models.CharField(max_length=4000, null=True, blank=True)
  is_template = models.BooleanField(default=False)
  '''