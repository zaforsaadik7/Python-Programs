"""
Make a to-do list manager in python where user should be avail to add tasks, mark as complete and view task.
Use a dictionary to store task, function to add task, mark as complete and view task.
Using dictionary, user can add additional details like task description, due date etc.
Ask user for task details and append them to the dictionary. Allow the user to mark the task by updating a "completed" status in the dictionary. 
Display the tasks with additional details.
"""
task={}

def add_task():
    task_name=input("enter task:")
    task_description=input('Enter task description:')
    due_date=input('Enter task date:')
    task[task_name]={"description":task_description, "Due date":due_date, 'complete':False}
    print('Task has benn added successfully.')

def mark_task():
        task_name=('Enter task to mark as complete.')
        if task_name in task:
            task[task_name]["complete"]= True
            print('Task marked as complete.')
        else:
            print('Task not found.')

def task_view():
    if not task:
        print('No task has been found.')
    else:
        for task_name, task_details in task.items():
            print('Name:', task_name)
            print('Description:', task_details['description'])
            print('Due_date:', task_details['Due date'])
            print('Status:', 'Completed.' if task_details['complete'] else 'Not complete yet.')

def main():
    while True:
        print('To-Do List Manager')
        print('1. Add task.')
        print('2. Mark task as complete.')
        print('3. View task.')
        choice=input('Enter your choice(1-4):')
        if choice == '1':
            add_task()
        elif choice == '2':
            mark_task()
        elif choice == '3':
            task_view()
        elif choice == '4':
            print('You have exited the program.')
            break
        else:
            print('Invalid Input.')
if __name__=="__main__":
    main()
