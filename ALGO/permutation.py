# Calculating permutation

n = int(input("please enter the value of n: "))
r = int(input("Please enter the value of r: "))


a = (n - r)
x = 1

for n in range(n, 0, -1):
    x *= n

y = 1    
for a in range(a, 0, -1):
    y *= a

nPr = x/y
print(nPr)
