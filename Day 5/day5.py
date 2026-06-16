employees = []

while True:
    print("\nEmployee management system")
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Exit")

    choice = int(input("Enter a choice:"))

    if choice == 1:
        name = input("Enter employee name:")
        employees.append(name)
        print("Employee added successfully")
    
    elif choice == 2:
        print("Employees list:")
        for i in employees:
            print(i)
    
    elif choice == 3:
        print("Exiting application")
        break
    else:
        print("Please enter a valid choice")