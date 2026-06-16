def add_employee(employee_list, name):
    employee_list.append(name)
    print("Employee Added")

def view_employee(employee_list):
    print("Employee list:")
    for i in employee_list:
        print(i)

def total_employees(employee_list):
    print("Total is:",len(employee_list))