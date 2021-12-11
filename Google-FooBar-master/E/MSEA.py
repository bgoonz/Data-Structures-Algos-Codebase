PREV_STATE = {
    ((0, 0), (0, 0)): 0,
    ((0, 0), (0, 1)): 1,
    ((0, 0), (1, 0)): 1,
    ((0, 0), (1, 1)): 0,
    ((0, 1), (0, 0)): 1,
    ((0, 1), (0, 1)): 0,
    ((0, 1), (1, 0)): 0,
    ((0, 1), (1, 1)): 0,
    ((1, 0), (0, 0)): 1,
    ((1, 0), (0, 1)): 0,
    ((1, 0), (1, 0)): 0,
    ((1, 0), (1, 1)): 0,
    ((1, 1), (0, 0)): 0,
    ((1, 1), (0, 1)): 0,
    ((1, 1), (1, 0)): 0,
    ((1, 1), (1, 1)): 0
}


CUR_STATE = {
    0: (
         ((0, 0), (0, 0)),
         ((0, 0), (1, 1)),
         ((0, 1), (0, 1)),
         ((0, 1), (1, 0)),
         ((0, 1), (1, 1)),
         ((1, 0), (0, 1)),
         ((1, 0), (1, 0)),
         ((1, 0), (1, 1)),
         ((1, 1), (0, 0)),
         ((1, 1), (0, 1)),
         ((1, 1), (1, 0)),
         ((1, 1), (1, 1))
       ),

    1: (
         ((1, 0), (0, 0)),
         ((0, 1), (0, 0)),
         ((0, 0), (1, 0)),
         ((0, 0), (0, 1))
       )
}

COL_CACHE = {}


def get_col_comb(first, column):
    x = ((0, 0), (0, 1), (1, 0), (1, 1))
    count_possibility = []
    for key in first:
        nextCol = []
        for val in x:
            if PREV_STATE[((key[0], key[1]), val)] == column[0]:
                nextCol.append(val)
        for n in range(1, len(column)):
            newCol = []
            if len(nextCol) == 0:
                break
            for col in nextCol:
                for m in range(2):
                    tempCol = list(col)
                    if PREV_STATE[((key[n], key[n+1]), (col[n], m))] == column[n]:
                        tempCol.append(m)
                        newCol.append(tempCol)
            nextCol = newCol
        [count_possibility.append((key, tuple(c))) for c in nextCol]
    return tuple(count_possibility)


def swap_row_col(g):
    return tuple(zip(*g))


def first_col_int(col):
    x = ((0, 0), (0, 1), (1, 0), (1, 1))
    present = CUR_STATE[col[0]]
    for n in range(1, len(col)):
        new = []
        for z in present:  # Each prev state for current state
            for comb in x:  # Every combination of bottom row of prev state
                #  Retains only combinations yielding next state in column
                if PREV_STATE[(z[n], comb)] == col[n]:
                    new.append(z[:]+(comb,))
        present = tuple(new)  # Builds column row by row
    return tuple([swap_row_col(x) for x in present])


def answer(g):
    rotation = swap_row_col(g)
    first = {}
    right_grids = first_col_int(rotation[0])  # Builds first column of preimages
    COL_CACHE[rotation[0]] = right_grids
    for z in right_grids:  # For each valid state in the top grid
        if z[1] not in first:  # Puts all bottom rows in dict and counts number of instances of each
            first[z[1]] = 1
        else:
            first[z[1]] += 1
    for n in range(1, len(rotation)):
        second = {}
        if rotation[n] in COL_CACHE:
            newGrids = COL_CACHE[rotation[n]]
        else:
            newGrids = first_col_int(rotation[n])  # Expands to next col to right in original grid/next down in transpose
            COL_CACHE[rotation[n]] = newGrids
        for z in newGrids:  # For each valid state in the bottom grid
            if z[0] in first:  # Checks for overlap between bottom row of state in 1st and top row of state in 2nd
                # Gives total number of states leading to particular bottom row of state in 2nd
                if z[1] in second:
                    second[z[1]] = first[z[0]] + second[z[1]]
                else:
                    second[z[1]] = first[z[0]]
        first = second
    return sum(first.values())  # Returns total possibilities yielding all bottom row states in transposed grid


