# Find the factorial of a user input (intiger)
number = int(input("Enter a number: "))
x = 1

for index in range(number, 0, -1):
    x *= index
    print(x )