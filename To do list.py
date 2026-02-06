task_to_do=[]
while True:
    print("\n1.Add,2.view ,3.update,4.Delete,5.Exit")
    A=input("enter choice:")
    if A=="1":
        task_to_do.append(input(" enter task:"))
        print("--task added--")
    elif A=="2":
        if not task_to_do:
            print("no task available")
        else:
            for i in range(len(task_to_do)):
                print(i+1,task_to_do[i])
    elif A=="3":
        if not task_to_do:
            print("no task to update")
        else:
            n=int(input("task number to update:"))
            if 1<=n <=len(task_to_do):
                task_to_do[n-1]=input("enter new task:")
                print("task updated")
            else:
                print("invalid task number")
    elif A=="4":
        if not task_to_do:
            print("no task to delete")
        else:
            n=int(input("task number to delete:"))
            if 1<=n<=len(task_to_do):
                task_to_do.pop(n-1)
                print("task deleted")
    elif A=="5":
        break
    else:
        print("invalid choice.choose correct one")