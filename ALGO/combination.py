# Calculation combination

n = int(input("Please enter the value of n: "))
r = int(input("Please enter the value of n: "))
x = 1

a = (n - r)

x = 1
for n in range(n, 0, -1):
    x *= n


y = 1
for a in range(a, 0, -2):
    y *= a

nPr = x/y


z = 1
for r in range(r, 0, -1):
    z *= r
nCr = nPr/z

print(nCr)