#The program calculates your BMI and returns the result

a= float(input("Type your weight \n"))
b= float(input("Type your height \n"))
bmi = a/b**2
print(bmi)
if (bmi <=5):
    print ("under weight")
if (bmi ==6)and (bmi<=24):
    print ("Normal weight")
if (bmi >=25):
    print ("obesity")