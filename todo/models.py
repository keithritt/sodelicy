from django.db import models


class Task(models.Model):
  STATUSES = (
    ('COM', 'Complete'),
    ('DEL', 'Deleted'),
    ('NEW', 'New'),
    ('FUT', 'Future'),
    ('CAN', 'Canceled'),
    ('INP', 'In Progress'),
  )
  CATEGORIES = (
    ('HOU', 'Housework'),
    ('PUR', 'Purchase List'),
    ('JLL', 'Work (JLL)'),
    ('FAM', 'Family'),
    ('HEA', 'Health'),
    ('LEA', 'Learning'),
    ('GDK', 'Gadake'),
    ('TF', 'Thirsty Flirt'),
    ('TODO', 'ToDo List App'),
  )
  ASSIGNEES = (
    ('KEI', 'Keith'),
    ('JES', 'Jess')
  )
  OCCURRENCES = (
    ('ONCE', 'One Time'),
    ('DAI', 'Daily'),
    ('WEE', 'Weekly'),
    ('MON', 'Monthy'),
    ('YEA', 'Yearly'),
  )
  PRIORITY = (
    ('URG', 'Urgent'),
    ('HIG', 'High'),
    ('MED', 'Medium'),
    ('LOW', 'Low'),
  )
  DURATIONS = (
    ('MIN', 'Minute'),
    ('HOUR', 'Hour'),
    ('DAY', 'Day'),
    ('WEEK', 'Week'),
    ('MON', 'Month'),
    ('YEAR', 'Year'),
  )
  text = models.CharField(max_length=128)
  #complete = models.BooleanField(default=False)
  status = models.CharField(max_length=4, choices=STATUSES, default='NEW', blank=True)
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

  def __str__(self):
    return "{} {} {}".format(self.priority, self.category, self.text)