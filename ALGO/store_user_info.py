# Prompt the user to enter a Surname
# Prompt the user to enter a Firstname
# Prompt the user to enter a Age
# Prompt the user to enter a location(city, country)
# Prompt the user to enter a Marital Status
# Prompt the user for thier BMI
# Print out the user information on seperate lines

print("Program to store and display a user information")

surName = input("Please enter your Surname: ")
firstName = input("Please enter your Firstname: ")
age = int(input("How old are you: "))
city = input("What city do you reside in: ")
country = input("What country do you reside in: ")
maritalStatus = input("Please enter your Marital Status: ")
bmi = float(input("Please enter your BMI: "))

print("\n USER INFORMATION \n")

print("Fullname: ", surName + " " + firstName)
print("Age: ", age)
print("Location: ", city + ", " + country)
print("Marital Status: ", maritalStatus)
print("BMI: ", bmi)
