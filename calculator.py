while True:
    a=float(input("Enter a value:"))
    b=float(input("Enter b value:"))
    print("select the operation?\n1.addition    2.subtraction\n3.multiplication     4.division\n        5.reminder")
    choice=int(input("Enter the choice:"))

    if choice==1:
        print(f"sum of {a} and {b} is:",a+b)
    elif choice==2:
        print(f"subtraction of {a} and {b} is:",a-b)
    elif choice==3:
        print(f"multiplication of {a} and {b} is:",a*b)
    elif choice==4:
        print(f"Division of {a} and {b} is:",a/b)
    elif choice==5:
        print(f"Reminder of {a} and {b} is:",a%b)
    else:
        print("Invalid choice")
        continue
    Next=input("Do you want to perform other operations?(Yes/No):")
    if Next!='Yes':
        break
