Amount = 7000
if Amount <= 4000:
    print("Move it to savings")
elif Amount == 5000:
    print("Buy fridge")
else:
    print("Send it to me")


def food():
    print("Had oats bowl in the morning")

food()

def food_break(phase):
    if phase.lower() == "breakfast":
        print("had oats bowl")
    elif phase.lower() == "lunch":
        print("had chapathi and dal")
    else:
        print("had dosa")

food_break("breakfast")
food_break("dinner")

def calculate_height(h1,h2):
    if h1>h2:
        return h1
    return h2

taller = calculate_height(152,165)
print("the tallest person is",taller)

def eligibility_check(experience):
    if experience >= 5:
        return "Eligible for job switch"
    else:
        return "Need more experience"

employee_name = "Lalitha"
work_experience = 2
result = eligibility_check(work_experience)

print("Employee:", employee_name)
print("Experience:", work_experience)
print("Result:", result)