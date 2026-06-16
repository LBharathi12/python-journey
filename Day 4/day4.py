name = input("Please enter your name:")
print("Good Morning",name)

experience = int(input("How many years of experience you have in  Python:"))
print("your experience is:",experience)

first_company = "TCS"
second_company = "CTS"

print("you have worked in",first_company+" and "+second_company)
print("first", first_company.lower())
print("second",second_company.lower())
print("name length is:",len(name))

weeks = ["monday","tuesday","wednesday","thursday","friday"]

def working_weeks(week_list):
    for week in week_list:
        print(week)
    
working_weeks(weeks)

skill_set = ['Python','Django','AWS']

def employee_details():
    print("\n Employee details:")
    print("Name:", name)
    print("Years of experience:",experience)
    if experience >= 5:
        print("Eligible")
    else:
        print("Need more experience")
    print("\nSkill set:")

    for skills in skill_set:
        print(skills)

employee_details()
