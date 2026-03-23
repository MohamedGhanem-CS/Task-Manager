tasks = []
username = input("Enter Your Name : ")
print(f"\nHello {username} Welcom to the road to success.")
# (loop)بدايه الابليكشن و اللوب اللي هنمشي عليه
while True:
    print("\n:Available Options:")
    print("1==> Add Task")
    print("2==> View Tasks")
    print("3==> Delete Task")
    print("4==> Exit from app")
    # (conditions)الحصول علي رقم العمليه من المستخدم وتنفيذها
    choice = input("\nSelect an operation (1-4): ")

    if choice == "1":
        task_name = input("Enter Task Name: ")
        importance = input("Assess the importance of the task: ")
        tasks.append({"name": task_name , "importance": importance})
        print("Task added successfully")

    elif choice == "2":
        print("\n Task List ")
        if not tasks:
            print("The list is empty.")
        else:
            for task in tasks:
                print(f" Task: {task["name"]} , importance : {task["importance"]}")
   
    elif choice == "3":
        if len(tasks) > 0:
            removed = tasks.pop(0)
            print("Deleted:", removed["name"])
        else:
            print("No tasks to delete")
    elif choice == "4":
        print("Exiting the program see you soon")
        break

    else:
        print("Wrong choice")
