from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import Task
from .forms import TaskForm, TaskEditForm

from pprint import pprint
import datetime
import json

from django.core import serializers


#@login_required
def index(request, filter=None):

  print(filter)
  if filter is None:
    task_model = Task.objects.exclude(status = 'COM')
  elif filter == 'work':
    task_model = Task.objects.filter(category="WOR").exclude(status = 'COM')
  elif filter == 'today':
    task_model = Task.objects.filter(start_date__lt=datetime.date.today() + datetime.timedelta(days=1))
  else:
    task_model = Task.objects.all()

  task_model.exclude(status='COM')

  task_model.order_by('-id')

  # create data to pass to js
  js_task_data = {}

  for task in task_model:
    tmp = {}
    tmp['status'] = task.status
    tmp['priority'] = task.priority
    tmp['category'] = task.category
    tmp['assignee'] = task.assignee
    tmp['occurence'] = task.occurence
    tmp['occurence_desc'] = task.occurence_desc
    tmp['percent_complete'] = task.percent_complete
    tmp['time_estimate_val'] = task.time_estimate_val
    tmp['time_estimate_metric'] = task.time_estimate_metric
    tmp['time_actual_val'] = task.time_actual_val
    tmp['time_actual_metric'] = task.time_actual_metric
    tmp['location'] = task.location
    #tmp['due_date_month'] = task.due_date_month
    #tmp['due_date_day'] = task.due_date_day
    #tmp['due_date_year'] = task.due_date_year


    js_task_data[task.id] = tmp;

  task_form = TaskForm()
  # show last task id info
  last_task_id = request.GET.get('last-task-id')
  if(last_task_id):
    task_obj = Task.objects.get(pk=last_task_id);
    task_form = TaskForm(request.POST, instance=task_obj)

  task_edit_form = TaskEditForm(auto_id='edit_task_%s')

  context = {
    'tasks' : task_model,
    'form' : task_form,
    'task_edit_form' : task_edit_form,
    'tasks_json': json.dumps(js_task_data)
  }

  return render(request, 'todo/index.html', context)


#@login_required
def calendar(request):
  #print(calendar);
  # get list of next 90 days
  dates = {}
  for x in range(91):
    tmp = {}
    #print(x)
    #pprint(datetime.timedelta(days=x))
    date = datetime.date.today() + datetime.timedelta(days=x)
    date_idx = date.__str__()
    tmp['display'] = date.strftime("%a %Y-%m-%d")
    #print(date)
    #print(date_idx)
    #print(date_display)
    dates[date_idx] = tmp

  #pprint(dates)


  #pprint(datetime.date.today())
  #pprint(datetime.timedelta(days=1))
  #pprint(datetime.date.today() + datetime.timedelta(days=1))


  #task_model = Task.objects.exclude(status = 'COM')

  task_form = TaskForm()



  context = {
    'dates' : dates,
    'form' : task_form
  }

  return render(request, 'todo/calendar.html', context)


@require_POST
#@login_required
# @todo - figure out how to make this work with both task
#using var task - it can represent either an Task object or a TaskForm
def saveTask(request):
  print('saveTask()')
  pprint(request.POST)
  task_id = request.POST.get('task-id')
  if(task_id == 'new'):
    print('new task')


    task_input = request.POST.get('task-input')

    task = Task(orig_text = task_input);
    #if task_input is not None:

    #elif:
    print(task_input)

    #task = TaskForm(request.POST)
    #task.save(commit=False) # the commit= false lets django know well be editing it more
    task.orig_text = task.text = request.POST['task-input']


    print('orig text: '+task.orig_text)


    #see if the text can be broken down into parts
    parts = request.POST['task-input'].split('|')
    del_parts = request.POST['task-input'].split('|') # it seems like running del on a part while iterating over it causes issue
    pprint(parts)
    #print(type(parts))
    #expose(parts)
    #print(parts[0])
    #parts.remove(0)
    #print(parts)

    part_idx = 0
    del_idx = 0 # super hacky - but it seems like the index of del_parts gets changed on each del - so part_idx is off
    for part in parts:
      part = part.lower()
      #print(part_idx)
      print(part)
      if(part == 'work'):
        #print('this is a category:jll item')
        task.category = 'WOR'
        del del_parts[del_idx]
        del_idx -= 1

        #print('adjusted task = ')
        #print('|'.join(del_parts))
        task.text = '|'.join(del_parts)

      if(part == 'me'):
        #print('this is an assignee:keith item')
        task.assignee = 'ME'
        del del_parts[del_idx]
        del_idx -= 1
        task.text = '|'.join(del_parts)
        #print(del_parts)

      if(part == 'spouse'):
        task.assignee = 'SPO'
        del del_parts[del_idx]
        del_idx -= 1
        task.text = '|'.join(del_parts)

      if(part == 'kid'):
        task.assignee = 'KID'
        del del_parts[del_idx]
        del_idx -= 1
        task.text = '|'.join(del_parts)

      if(part == 'urgent'):
        task.priority = 'URG'
        del del_parts[del_idx]
        del_idx -= 1
        task.text = '|'.join(del_parts)

      if(part == 'high'):
        #print('this is an priority:high item')
        task.priority = 'HIG'
        #print(del_parts)
        del del_parts[del_idx]
        del_idx -= 1
        task.text = '|'.join(del_parts)

      if(part == 'medium'):
        task.priority = 'MED'
        del del_parts[del_idx]
        del_idx -= 1
        task.text = '|'.join(del_parts)

      if(part == 'low'):
        task.priority = 'LOW'
        del del_parts[del_idx]
        del_idx -= 1
        task.text = '|'.join(del_parts)


      if(part == 'todo'):
        task.category = 'TODO'
        del del_parts[del_idx]
        del_idx -= 1
        task.text = '|'.join(del_parts)

      if(part == 'home'):
        task.category = 'HOU'
        del del_parts[del_idx]
        del_idx -= 1
        task.text = '|'.join(del_parts)

      if(part == 'buy'):
        task.category = 'PUR'
        del del_parts[del_idx]
        del_idx -= 1
        task.text = '|'.join(del_parts)

      if(part == 'daily'):
        task.occurence = 'DAI'
        del del_parts[del_idx]
        del_idx -= 1
        task.text = '|'.join(del_parts)

      if(part == 'nightly'):
        task.occurence = 'DAI'
        task.occurence_desc = 'Nightly'
        del del_parts[del_idx]
        del_idx -= 1
        task.text = '|'.join(del_parts)

      if(part == 'morning'):
        task.occurence = 'DAI'
        task.occurence_desc = 'Every Morning'
        del del_parts[del_idx]
        del_idx -= 1
        task.text = '|'.join(del_parts)

      if(part == 'weekly'):
        task.occurence = 'WEE'
        del del_parts[del_idx]
        del_idx -= 1
        task.text = '|'.join(del_parts)

      if(part == 'monthly'):
        task.occurence = 'MON'
        del del_parts[del_idx]
        del_idx -= 1
        task.text = '|'.join(del_parts)

      part_idx +=1
      del_idx += 1
      '''
    #print(parts[0].lower())
    if(parts[0].lower() == 'jll'):
      print('this is a jll task');
      form.category = 'JLL'
      #parts.remove(0)
      print(parts)
      print('|'.join(parts))
      form.text = form
    else:
      print('this is not a JLL task')

      '''
  else:
    print('task_id: ')
    pprint(task_id)
    task = Task.objects.get(pk=task_id);
    pprint(task)
    print(task.text);
    #task = TaskForm(request.POST, instance=task)


  print(task.category)
  print(task.text)
  print(task.orig_text)



  #newtodoform = NewTodoForm(request.POST, instance=todo_13)

  #if(form.is_valid()):
      #new_todo = Todo(text=form.cleaned_data['text'])
      #new_todo.save()
      #pass
      # - avoid saving for now todo =
  print('saving task...')
  task.save()
  print('task saved')

  pprint(task)
  print('task id = {}'.format(task.id) )

  new_task = Task.objects.get(pk=task.id);

  print('new task = ')
  print(new_task)

  #return HttpResponse('done')
  return redirect("/todo?last-task-id={}".format(task.id))

#@login_required
def viewTask(request, task_id):
  print('viewTask()')
  print(task_id)
  if(task_id == 'new'):
    form = TaskForm()
  else:
    task = Tasks.objects.get(pk=task_id);
    form = TaskForm(instance=task)

  #todo - figure out how to pass task_id as a hidden field
  context = {
    'task_id' : task_id,
    'form' : form
  }
  return render(request, 'todo/view_task.html', context)

#@login_required
#@require_POST
@csrf_exempt # easier to debug with it off
def util(request, action=None):
  print('view.util()')

  if action == 'mark-task-complete':
    task = Task.objects.get(pk=request.POST.get('task_id'));
    if request.POST.get('completed'):
      task.status = 'COM'
    else:
      task.status = 'NEW' # assume new for now
    pprint(task)

    task.save();
  elif action == 'add-to-queue':
    task = Task.objects.get(pk=request.POST.get('task_id'));
    task.start_date = datetime.datetime.now()
    task.save();
  elif action == 'remove-from-queue':
    task = Task.objects.get(pk=request.POST.get('task_id'));
    task.start_date = None
    task.save();







  return HttpResponse('Task saved.')