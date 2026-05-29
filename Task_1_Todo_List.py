# To-do List
while True:
    with open("tasklist.txt","a+") as file:
        print("\n\tMenu")
        print("1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit\n")
        try:
            ch=int(input("Enter your choice : "))
        except Exception as e:
            print("Enter only integer value")
            continue

        if ch==1:   # Writing
            taketask=str(input("Enter you Task : "))
            file.write(f"{taketask}\n")
            print("Task added in To-do list")

        elif ch==2: # Reading
            file.seek(0)
            r=file.readlines()
            print("Your To-do list :")
            for i,j in enumerate(r,start=1):
                print(f"{i}. {j}",end="")
            print("----------------")
            
        elif ch==3: # removing
            file.seek(0)
            r=file.readlines()
            rem=int(input("Enter the Task no. to remove : "))
            rem-=1
            print(f"removed : {r[rem]}")
            r.pop(rem)
            with open("tasklist.txt","w") as file:
                for i in r:
                    file.write(i)
                
        elif ch==4: # Exit
            print("Exited !")
            break

        else:
            print("Wrong choice ! Enter from Menu")