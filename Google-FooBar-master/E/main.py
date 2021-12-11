import My_Expanding_Nebula as my
import test_nebula as prv
import NK_MANSON as NK
import MSEA as NEW
import random
import time

rnd = random.Random()

def test(x,y,trials):

    t1,t2,t3 = 0,0,0
    
    for i in range(trials):
        ls = [[(True if rnd.randint(0,1) else False) for i in range(y)] for j in range(x)]

        init = time.clock()
        r1 = NEW.answer(ls)
        t1 += ( time.clock() - init )
        
        init = time.clock()
        r2 = my.answer(ls)
        t2 += ( time.clock() - init )

        init = time.clock()
        r3 = NK.answer(ls)
        t3 += ( time.clock() - init )
        

        if not (r1==r2 and r2==r3 and r1==r3) :
           print('ERROR!!',r1,r2,r3)

    return t2,t3,t1

def f(x,X,y,Y,T):
    v1,v2,v3 = 0,0,0
    t1,t2,t3 = 0,0,0
    
    for i in range(x,X+1):
        print('\n',i)
        for j in range(y,Y+1):
            print(j,end=',')
            a,b,c = test(i,j,T)
            t1+=a
            t2+=b
            t3+=c
            val = min(a,b,c)
            if val==a:
                v1+=1
            elif val==b:
                v2+=1
            else:
                v3+=1
    print('\n' , (v1,v2,v3) , (t1,t2,t3) )
            
