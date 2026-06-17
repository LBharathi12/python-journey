with open("employee_data.txt","w") as file:
    file.write("I am learning about file handling")

with open("employee_data.txt","r") as file:
    content = file.read()
    print(content)

with open("employee_data.txt","a") as file:
    file.write("\nIn write mode,everytime we run, Old content removed and new content is written")

name = input("Are you a human? ")
with open ("employee_data.txt","a") as file:
    file.write("\nWelcome to the course\n")

print("Please go ahead")


print("Welcome to employee management system")
while True:
    print("1.Add Employee")
    print("2. View Employee details")
    print("3. Exit")
    choice = int(input("Please enter your choice:"))

    if choice == 1:
        emp_name = input("Please enter your name:")
        with open("employee_data.txt","a") as file:
            file.write(emp_name+"\n")
        print("Employee details saved successfully!!")

    elif choice == 2:
        with open("employee_data.txt","r") as file:
            file_contents = file.read()
            print("File details:\n",file_contents)
    
    elif choice == 3:
        print("Thank you")
        break

    else:
        print("Please enter a right choice")