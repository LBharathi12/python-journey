to_buy = ["Fridge", "Television", "Chimney", "Ac"]
print("The created list:", to_buy)
print("First thing to buy:", to_buy[0])
print("Second thing to buy:", to_buy[2])

My_details = {"Name":"lalitha", "Age":27, "Work":"IT"}
print("This is about me:", My_details)
print("My name is:", My_details["Name"])
print("I am "+ str(My_details["Age"]) +" years old\n")

print("Objects to buy for our new home:")
for obj in to_buy:
    print(obj)


work_exp = [
    {
        "Company_name":"TCS",
        "Period": 4
    },
    {
        "Company_name":"CTS",
        "Period": 1
    }
]

print("\nCompanies I have worked so far:")
for place in work_exp:
    print(place["Company_name"])