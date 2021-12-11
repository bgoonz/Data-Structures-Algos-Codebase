#FINDING PROBABILITY OF VERTEX IN GRAPH, REACHABLE FROM FIRST NODE 
from fractions import Fraction as frct

def matinv(mat):
    n=len(mat)
    matinv=[[ (0 if i!=j else 1) for i in range(n)] for j in range(n)]
    for i in range(n):
        if mat[i][i]==0:
            for j in range(n):
                if mat[j][i]!=0:
                    (mat[i],mat[j])=(mat[j],mat[i])
                    (matinv[i],matinv[j])=(matinv[j],matinv[i])
                    break
        f=mat[i][i]
        if f!=1:
            for j in range(n):
                mat[i][j]/=f
                matinv[i][j]/=f
        for j in range(n):
            if j!=i:
                if mat[j][i]!=0 :
                    a=mat[j][i]
                    for k in range(n):
                        mat[j][k]-=a*mat[i][k]
                        matinv[j][k]-=a*matinv[i][k]    
    return matinv

def answer(ls):
    ln = len(ls)
    lmt = 1
    for i in range(ln):
        k = sum(ls[i])
        if k!=0:
            lmt*=k
            for j in range(ln):
                ls[i][j] /= k

    trmnls = [i for i in range(ln) if sum(ls[i])==0]
    non_trmnls = [i for i in range(ln) if i not in trmnls]

    ln_trmnl = len(trmnls)
    ln_nontrmnl = len(non_trmnls)

    if sum(ls[0])==0:#No way from root itself
        return [1]+[0 for i in range(ln_trmnl-1)]+[1]

    ls2 = [[(-ls[i][j] if i!=j else 1) for i in range(ln) if i in non_trmnls] for j in range(ln) if j in non_trmnls]

    ls3 = matinv(ls2)
    
    c,prob = 0,[]
    for i in range(ln):
        if i in trmnls:
            prob.append(0.0)
        else:
            prob.append(ls3[c][0])
            c+=1

    for i in range(ln):
        if i in trmnls:
            prob[i] = sum([(ls[j][i]*prob[j])for j in range(ln)])

    dnm = max([frct(prob[i]).limit_denominator(lmt).denominator for i in range(ln) if i in trmnls])
    return [round(prob[i]*dnm) for i in trmnls]+[dnm]
