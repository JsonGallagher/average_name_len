avg_american_name_len = 3
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
full_name = first_name + last_name

if len(full_name) == 10:
    print("Your name " + first_name + " " + last_name + " is exactly the average American name with 10 characters.")
elif len(full_name) > 10:
    print("Your name " + first_name + " " + last_name + " is longer than the average American name")
else:
    print("Your name " + first_name + " " + last_name + " is shorter than the average American name")