# Generated by Django 2.2.2 on 2019-06-12 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_task_is_template'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='is_template',
        ),
        migrations.RemoveField(
            model_name='task',
            name='start_date',
        ),
        migrations.AlterField(
            model_name='task',
            name='assignee',
            field=models.CharField(blank=True, choices=[('KEI', 'Keith'), ('JES', 'Jess')], default='KEI', max_length=4, null=True),
        ),
    ]
