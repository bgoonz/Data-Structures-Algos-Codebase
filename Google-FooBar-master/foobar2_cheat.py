from fractions import Fraction as frct

def inv(mtrx):
    n = len(mtrx)
    invrs = [[frct(0) for col in range(n)] for rw in range(n)]
    for i in range(n):
        invrs[i][i] = frct(1)
    for i in range(n):
        for j in range(n):
            if i != j:
                if mtrx[i][i] == 0:
                    return false
                rtn = mtrx[j][i] / mtrx[i][i]
                for k in range(n):
                    invrs[j][k] = invrs[j][k] - rtn * invrs[i][k]
                    mtrx[j][k] = mtrx[j][k] - rtn * mtrx[i][k]
    for i in range(n):
        a = mtrx[i][i]
        if a == 0:
            return false
        for j in range(n):
            invrs[i][j] = invrs[i][j] / a
    return invrs


def answer(ls):
    if len(ls) < 2:
        return [-1, -1]
    if len(ls) == 2:
        x = (frct(ls[1] - ls[0]) / frct(3)) * frct(2)
        if (x.numerator < 1) or (x.numerator < x.denominator):
            return [-1, -1]
        return [x.numerator, x.denominator]

    mtrx = []
    rowNum = 0
    dlts = []
    for loc in ls:
        dlts.append(frct(ls[rowNum + 1] - ls[rowNum]))
        if rowNum == 0:
            rw = [frct(2), frct(1)] + [frct(0)] * (len(ls) - 3)
            mtrx.append(rw)
        elif rowNum == len(ls) - 2:
            rw = [frct(1)] + [frct(0)] * (len(ls) - 3) + [frct(1)]
            mtrx.append(rw)
            break
        else:
            rw = [frct(0)] * rowNum + [frct(1), frct(1)] + [frct(0)] * (len(ls) - rowNum - 3)
            mtrx.append(rw)
        rowNum = rowNum + 1

    invrs = inv(mtrx)
    if not(invrs):
        return [-1, -1]
    #For Validating every gear
    for i in range(1, len(ls)-1):
        y = frct(0)
        for j in range(len(ls)-1):
            y = y + invrs[i][j] * dlts[j]
        if (y.numerator < 1) or (y.numerator < y.denominator):
            return [-1, -1]

    x = frct(0)
    for i in range(len(ls)-1):
        x = x + invrs[0][i] * dlts[i]
    x = x * frct(2)

    if (x.numerator < 1) or (x.numerator < x.denominator):
        return [-1, -1]
    return [x.numerator, x.denominator]
