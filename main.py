from todoist_api_python.api import TodoistAPI
from settings import api_token
import sys
import json

api = TodoistAPI(api_token)
err_help_message = 'Invalid input!\nUsage:\ntodo "<task_contents_here>"'

if len(sys.argv) == 2:
    try:
        projects = api.get_projects()
        for i in range(len(projects)):
            if projects[i].is_inbox_project == True:
                inbox_project_id = projects[i].id
                inbox_project_name = projects[i].name
    except Exception as error:
        print(error)

    if inbox_project_id:
        try:
            task = api.add_task(content=sys.argv[1], project_id=inbox_project_id, due_string = 'today')
            new_task_id = str(task.id)
            new_task_created_date = str(task.created_at).split('.')[0].replace('T',' ')
            new_task_project_name = api.get_project(project_id=task.project_id).name
            new_task_due = str(task.due.date)
            print('Task created in: %s\nCreated: %s\nDue: %s' % (new_task_project_name, \
                                                                new_task_created_date, \
                                                                new_task_due))
        except Exception as error:
            print(error)
else:
    print(err_help_message)
    sys.exit(1)
