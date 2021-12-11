#FINDING CODE, when CO-ORDINATES ARE GIVEN
def answer(x,y):
    s = 0
    for i in range(1,x+1):
        s+=i
    for i in range(x,x+y-1):
        s+=i
    return str(s)
