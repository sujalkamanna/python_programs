def task():
    tasks = []
    print("WELCOME TO TASK MANAGER")

    total_tasks = int(input("Enter no of tasks you want to Enter:"))
    for i in range(1, total_tasks+1):
        task_name = input(f"Enter your task {i}:")
        tasks.append(task_name)

    print("todays tasks are as follows ", tasks)
    while True:
        operations = int(
            input('''\nOperations:\n1.Add Task\n2.Update\n3.Delete\n4.View \n5. Exit/Stop.\nEnter operations you want ot perform :'''))

        if operations == 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print("task", add, "has been added successfully.")
        elif operations == 2:
            update = input("Enter task you want to update = ")
            if update in tasks:
                index = tasks.index(update)
                new_task = input("Enter the new task: ")
                tasks[index] = new_task
                print("Task updated successfully")
            else:
                print("Task not present !")
        elif operations == 3:
            delete = input("Enter task you want to delete = ")
            tasks.remove(delete)
            print("Task deleted successfully")
        elif operations == 4:
            print("Yours tasks are as follows:")
            for j in tasks:
                print(j,end=",")
        elif operations == 5:
            print('Exiting Task Manager.')
            break
        else:
            print("Invalid Input")


task()
