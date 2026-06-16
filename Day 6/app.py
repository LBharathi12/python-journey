from employee_service import add_employee, view_employee, total_employees
employee = []

while True:
    print("\nWelcome to employee management")
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Exit application")
    print("4. Total Employees")
    print("\n")
    choice = int(input("Please enter your choice:"))

    if choice == 1:
        name = input("Enter your name: ")
        add_employee(employee,name)
    elif choice == 2:
        view_employee(employee)
    elif choice == 3:
        break
    elif choice == 4:
        total_employees(employee)
    else:
        print("Please enter a valid choice")