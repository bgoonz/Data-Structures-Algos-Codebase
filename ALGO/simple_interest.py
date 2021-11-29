# Ask the user to input the principal amount
# Ask the user to enter the rate
# Ask user to input the time period
# Calculate simple interest
# print simple interest

principal_amount = float(input("Type your principal amount \n"))
rate = float(input("Type your rate \n"))
time_period = float(input("Type the time peroid \n"))

interest = (principal_amount * rate * time_period) / 100
print(round(interest, 2))