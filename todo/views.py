from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.http import require_POST

from .models import Task
from .forms import *

def index(request):
  tasks = Task.objects.order_by('id')


  form = TaskForm()

  context = {
    'tasks' :  tasks,
    'form' : form
  }

  return render(request, 'todo/index.html', context)

@require_POST
def saveTask(request):
  #print(request.POST)
  task_id = request.POST.get('task_id')
  if(task_id == 'new'):
    form = TaskForm(request.POST)
    task_form = form.save(commit=False) # the commit= false lets django know well be editing it more
    task_form.orig_text = request.POST['text']

    #see if the text can be broken down into parts
    parts = request.POST['text'].split('|')
    del_parts = request.POST['text'].split('|') # it seems like running del on a part while iterating over it causes issue
    #print(parts)
    #print(type(parts))
    #expose(parts)
    #print(parts[0])
    #parts.remove(0)
    #print(parts)

    part_idx = 0
    del_idx = 0 # super hacky - but it seems like the index of del_parts gets change on each del - so part_idx is off
    for part in parts:
      part = part.lower()
      #print(part_idx)
      #print(part)
      if(part == 'jll'):
        #print('this is a category:jll item')
        task_form.category = 'JLL'
        del del_parts[del_idx]
        del_idx -= 1

        #print('adjusted task = ')
        #print('|'.join(del_parts))
        task_form.text = '|'.join(del_parts)

      if(part == 'keith'):
        #print('this is an assignee:keith item')
        task_form.assignee = 'KEI'
        del del_parts[del_idx]
        del_idx -= 1
        task_form.text = '|'.join(del_parts)
        #print(del_parts)

      if(part == 'urgent'):
        task_form.priority = 'URG'
        del del_parts[del_idx]
        del_idx -= 1
        task_form.text = '|'.join(del_parts)

      if(part == 'high'):
        #print('this is an priority:high item')
        task_form.priority = 'HIG'
        #print(del_parts)
        del del_parts[del_idx]
        del_idx -= 1
        task_form.text = '|'.join(del_parts)

      if(part == 'medium'):
        task_form.priority = 'MED'
        del del_parts[del_idx]
        del_idx -= 1
        task_form.text = '|'.join(del_parts)

      if(part == 'low'):
        task_form.priority = 'LOW'
        del del_parts[del_idx]
        del_idx -= 1
        task_form.text = '|'.join(del_parts)

      if(part == 'gadake'):
        task_form.category = 'GDK'
        del del_parts[del_idx]
        del_idx -= 1
        task_form.text = '|'.join(del_parts)

      if part in ['tf', 'thirsty']:
        task_form.category = 'TF'
        del del_parts[del_idx]
        del_idx -= 1
        task_form.text = '|'.join(del_parts)

      if(part == 'todo'):
        task_form.category = 'TODO'
        del del_parts[del_idx]
        del_idx -= 1
        task_form.text = '|'.join(del_parts)

      if(part == 'home'):
        task_form.category = 'HOU'
        del del_parts[del_idx]
        del_idx -= 1
        task_form.text = '|'.join(del_parts)

      if(part == 'buy'):
        task_form.category = 'PUR'
        del del_parts[del_idx]
        del_idx -= 1
        task_form.text = '|'.join(del_parts)

      if(part == 'daily'):
        task_form.occurence = 'DAI'
        del del_parts[del_idx]
        del_idx -= 1
        task_form.text = '|'.join(del_parts)

      if(part == 'nightly'):
        task_form.occurence = 'DAI'
        task_form.occurence_desc = 'Nightly'
        del del_parts[del_idx]
        del_idx -= 1
        task_form.text = '|'.join(del_parts)

      if(part == 'morning'):
        task_form.occurence = 'DAI'
        task_form.occurence_desc = 'Every Morning'
        del del_parts[del_idx]
        del_idx -= 1
        task_form.text = '|'.join(del_parts)

      if(part == 'weekly'):
        task_form.occurence = 'WEE'
        del del_parts[del_idx]
        del_idx -= 1
        task_form.text = '|'.join(del_parts)

      if(part == 'monthly'):
        task_form.occurence = 'MON'
        del del_parts[del_idx]
        del_idx -= 1
        task_form.text = '|'.join(del_parts)



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
    task = Task.objects.get(pk=task_id);
    print(task)
    print(task.text);
    form = TaskForm(request.POST, instance=task)


  print(task_form.category)
  print(task_form.text)
  print(task_form.orig_text)



  #newtodoform = NewTodoForm(request.POST, instance=todo_13)

  if(form.is_valid()):
      #new_todo = Todo(text=form.cleaned_data['text'])
      #new_todo.save()
      #pass
      # - avoid saving for now todo =
      task_form.save()

  #return HttpResponse('done')
  return redirect('view_task', 'new')


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