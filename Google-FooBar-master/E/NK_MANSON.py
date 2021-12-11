box = {
    ((0, 0), (0, 0)) : 0,
    ((0, 0), (0, 1)) : 1,
    ((0, 0), (1, 0)) : 1,
    ((0, 0), (1, 1)) : 0,
    ((0, 1), (0, 0)) : 1,
    ((0, 1), (0, 1)) : 0,
    ((0, 1), (1, 0)) : 0,
    ((0, 1), (1, 1)) : 0,
    ((1, 0), (0, 0)) : 1,
    ((1, 0), (0, 1)) : 0,
    ((1, 0), (1, 0)) : 0,
    ((1, 0), (1, 1)) : 0,
    ((1, 1), (0, 0)) : 0,
    ((1, 1), (0, 1)) : 0,
    ((1, 1), (1, 0)) : 0,
    ((1, 1), (1, 1)) : 0,
}



true = True
false = False


def get_col_comb(first,column):
    x = ((0,0),(0,1),(1,0),(1,1))
    count_possibility = []

    for key in first:
        nextCol = []

        for val in x:
            if box[((key[0],key[1]),val)] == column[0]:
                nextCol.append(val)

        for n in range(1,len(column)):
            newCol = []
            if len(nextCol) == 0:
                break
            for col in nextCol:
                for m in range(2):
                    tempCol = list(col)
                    if box[((key[n],key[n+1]),(col[n],m))] == column[n]:
                        tempCol.append(m)
                        newCol.append(tempCol)
            nextCol = newCol
        [count_possibility.append((key,tuple(c))) for c in nextCol]
    return tuple(count_possibility)

def swap_row_col(g):
    return tuple(zip(*g))

def nk(firstColumn):
    def first_col_int(f_c_col):
        def initialize(col):
            g0 = col[0]
            l = []
            for key,val in box.items():
                if g0 == val:
                    l.append(key)
            return tuple(l)

        x = ((0,0),(0,1),(1,0),(1,1))
        present = initialize(f_c_col)
        for n in range(1,len(f_c_col)):
            new = []
            for z in present:
                for comb in x:
                    possibility = (z[n],comb)

                    if box[possibility] == f_c_col[n]:
                        temp = list(z)
                        temp.append(comb)
                        new.append(temp)

            present = tuple(new)
        return tuple([swap_row_col(x) for x in present])

    if firstColumn in no_col:
        return no_col[firstColumn]
    else:
        right_grids = first_col_int(firstColumn)
        no_col[firstColumn] = right_grids
        return right_grids

def counter(g):
    rotation = swap_row_col(g)
    first = {}
    right_grids = nk(rotation[0])
    for z in right_grids:
        if z[1] not in first:
            first[z[1]] = 1
        else:
            first[z[1]] = first[z[1]] + 1
    for n in range(1,len(rotation)):
        second = {}
        newGrids = get_col_comb(first,rotation[n])
        total = len(newGrids)
        for z in newGrids:
            isValid_counter = 0
            if z[0] in first:
                isValid_counter += 1
                if z[1] in second:
                    second[z[1]] = first[z[0]] + second[z[1]]
                else:
                    second[z[1]] = first[z[0]]
        first = second
    meter = 0
    for row, count in first.items():
        meter += count
    return meter

no_col = {}

def answer(g):
    return counter(g)
