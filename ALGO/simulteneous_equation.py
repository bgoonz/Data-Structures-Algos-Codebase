# solving simultaneous equation using python

print('For equation 1')
a = int(input("Type the coefficient of x = \n"))
b = int(input("Type the coefficient of y = \n"))
c = int(input("Type the coefficient of the constant, k = \n"))
print("For equation 2")
d = int(input("Type the coefficient of x = \n"))
e = int(input("Type the coefficient of y = \n"))
f = int(input("Type the coefficient of the constant, k = \n"))

def determinant():
    return((a*e) - (b*d))
    
x = determinant()
# print(x) to output: a*e - b*d
def cofactors():
    return((e*c) + (-1 * d * f)) / determinant(), ((-1 * b * c) + (a * 5)) / determinant()
    
z = cofactors()
#print(z) output: (e*c) + (-1 * d * f) / determinant(), ((-1 * b * c) + (a * 5)) / determinant()
print("Answer = (x,y)")
print(cofactors())
