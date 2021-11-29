# Write the purpose of the program
# prompt the user for a valid user name
# print a welcome to the user
# Prompt the user to enter a value
# print out the multiplication table for that number
# End program

print("This program displays the Multiplication table for a number")
userName = input("Please enter your name: ")
print("Welcome ", userName)
value = int(input("Please enter a number: "))
for i in range(1, 13, 1):
    print(value, "*", i, "=", value*i)

print("You now have your Multiplication table so the program has ended")
