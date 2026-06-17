try:
    age = int(input("Enter your age:"))
    print("Your age is:",age)
except ValueError:
    print("Age should be in numbers")

print("Employee eligibility checker v2")


emp_name = input("Enter your name:")
try:
    exp = int(input("Enter your experience:"))
    if exp >= 5:
        print("Eligible")
    else:
        print("Need more experience")
except ValueError:
    print("Please enter a valid number")

print("******** Welcome to Employee Management System V4 **********")
name_list = []
try:
    while True:
        choice = int(input("Enter your choice:"))
        if choice == 1:
            name = input("enter your name:")
            name_list.append(name)
        elif choice == 2:
            print("The employee list:")
            for i in name_list:
                print(i)
        elif choice == 3:
            print("Exiting the application")
            break
        else:
            print("Invalid choice")
except:
    print("Invalid choice")
