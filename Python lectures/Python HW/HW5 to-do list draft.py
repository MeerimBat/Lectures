#Project:
 #imple To-Do List. Create a program that allows a user to manage a to-do list. The user should be able to:
#Add a new task.
#View all tasks.
 #elete a task by its name or number.
#The program should loop until the user decides to quit.
to_do_list = ["1Watch the lectures", "2Do the homework", "3Call your study buddy"]
tasks =str(input)
print(to_do_list)
item=input("Enter a new task")
to_do_list.append(item)
print("Uppdates list:",to_do_list)
task_to_remove=input("Enter the task to remove")
if task_to_remove in to_do_list:
     to_do_list.remove(task_to_remove)
     print(f"{task_to_remove}has been deleted. Updated list:{to_do_list}")
else: 
     print(f"task_to_remove is not in the list")