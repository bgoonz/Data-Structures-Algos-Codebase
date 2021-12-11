"""
    by: zimmerk4@msu.edu
    
    Expanding Nebula
    ================
    You've escaped Commander Lambda's exploding space station along with numerous escape pods full of bunnies.
    But - oh no! - one of the escape pods has flown into a nearby nebula, causing you to lose track of it. You start
    monitoring the nebula, but unfortunately, just a moment too late to find where the pod went. However, you do find
    that the gas of the steadily expanding nebula follows a simple pattern, meaning that you should be able to determine
    the previous state of the gas and narrow down where you might find the pod.
    From the scans of the nebula, you have found that it is very flat and distributed in distinct patches, so you can
    model it as a 2D grid. You find that the current existence of gas in a cell of the grid is determined exactly by its
    4 nearby cells, specifically, (1) that cell, (2) the cell below it, (3) the cell to the right of it, and (4) the
    cell below and to the right of it. If, in the current state, exactly 1 of those 4 cells in the 2x2 block has gas,
    then it will also have gas in the next state. Otherwise, the cell will be empty in the next state.
    For example, let's say the previous state of the grid (p) was:
    .O..
    ..O.
    ...O
    O...
    To see how this grid will change to become the current grid (c) over the next time step, consider the 2x2 blocks of
    cells around each cell.  Of the 2x2 block of [p[0][0], p[0][1], p[1][0], p[1][1]], only p[0][1] has gas in it, which
    means this 2x2 block would become cell c[0][0] with gas in the next time step:
    .O -> O
    ..
    Likewise, in the next 2x2 block to the right consisting of [p[0][1], p[0][2], p[1][1], p[1][2]], two of the
    containing cells have gas, so in the next state of the grid, c[0][1] will NOT have gas:
    O. -> .
    .O
    Following this pattern to its conclusion, from the previous state p, the current state of the grid c will be:
    O.O
    .O.
    O.O
    Note that the resulting output will have 1 fewer row and column, since the bottom and rightmost cells do not have a cell below and to the right of them, respectively.
    Write a function answer(g) where g is an array of array of bools saying whether there is gas in each cell (the current scan of the nebula),
    Languages
    =========
    To provide a Python solution, edit solution.py
    To provide a Java solution, edit solution.java
    Test cases
    ==========
    Inputs:
        (boolean) g = [
                        [true, false, true],
                        [false, true, false],
                        [true, false, true]
                      ]
    Output:
        (int) 4
    Inputs:
        (boolean) g = [
                        [true, false, true, false, false, true, true, true],
                        [true, false, true, false, false, false, true, false],
                        [true, true, true, false, false, false, true, false],
                        [true, false, true, false, false, false, true, false],
                        [true, false, true, false, false, true, true, true]
                      ]
    Output:
        (int) 254
    Inputs:
        (boolean) g = [
                        [true, true, false, true, false, true, false, true, true, false],
                        [true, true, false, false, false, false, true, true, true, false],
                        [true, true, false, false, false, false, false, false, false, true],
                        [false, true, false, false, false, false, true, true, false, false]
                      ]
    Output:
        (int) 11567
"""
import unittest
import random
import itertools


def transpose(arry):
    return map(list, zip(*arry))


def build_grid_states(grid):
    """ Takes a grid as a 2D binary array and returns a dictionary of key=(i,j) and value=states to represent the 2x2
    state at any given location of the original grid."""
    state_ary = {}
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == 1:  # Trailing comma to force the tuple of tuple structure for single element cases
                state_ary[(i, j)] = {((1, 0),): ((0, 0),),
                                     ((0, 1),): ((0, 0),),
                                     ((0, 0),): ((1, 0), (0, 1))}
            else:
                state_ary[(i, j)] = {((1, 1),): ((1, 1), (1, 0), (0, 1), (0, 0)),
                                     ((0, 1),): ((1, 1), (0, 1), (1, 0)),
                                     ((1, 0),): ((1, 1), (1, 0), (0, 1)),
                                     ((0, 0),): ((1, 1), (0, 0))}
    return state_ary


def find_valid_col_states(grid):
    state_ary = build_grid_states(grid)
    valid_col_states = {}
    temp_col_states = {}
    for j in range(len(grid[0])):
        valid_col_states[j] = state_ary[(0, j)]
        for i in range(len(grid) - 1):
            for key, value in valid_col_states[j].items():
                for elem in value:  # Checks for all bottom rows of first state
                    if (elem,) in state_ary[(i + 1, j)]:  # Checks if bottom row 1st state same as top row of 2nd state
                        temp_col_states[(key[:] + (elem,))] = state_ary[(i + 1, j)][(elem,)]
            valid_col_states[j] = temp_col_states
            temp_col_states = {}
    return valid_col_states


def split_col(col):
    l_r_dict = {}
    for key_1, value_1 in col.items():
        for val_row in value_1:
            temp_r = ()
            temp_l = ()
            for key_row in key_1:
                temp_r += (key_row[-1],)
                temp_l += key_row[:-1]
            temp_r += (val_row[-1],)
            temp_l += val_row[:-1]
            if (temp_l,) in l_r_dict:
                l_r_dict[(temp_l,)] += (temp_r,)
            else:
                l_r_dict[(temp_l,)] = (temp_r,)
    return l_r_dict


# def compare_cols(col_1, col_2):
#     col_1_splt = split_col(col_1)
#     col_2_splt = split_col(col_2)
#     valid_col_states = {}
#     for key, value in col_1_splt.items():
#         for elem in value:  # Checks for all cols of first col
#             if (elem,) in col_2_splt:  # Checks if right col of 1st col state is same as left col of 2nd col state
#                 valid_col_states[(key[:] + (elem,))] = col_2_splt[(elem,)]
#     return valid_col_states


def compare_cols(col_1, col_2):
    # col_1_splt = split_col(col_1)
    # col_2_splt = split_col(col_2)
    valid_col_states = {}
    for key, value in col_1.items():
        for elem in value:  # Checks for all cols of first col
            for key_2 in col_2.keys():  # Checks if right col of 1st col state is same as left col of 2nd col state
                if elem == key_2[0]:
                    valid_col_states[(key[:] + (elem,) + key_2[1:])] = col_2[key_2]
    return valid_col_states


# def find_valid_grid_states(grid):
#     cols_states = find_valid_col_states(grid)
#     valid_grid_states = {}  # Storage container for valid grids. Starts as split columns
#     for key, value in cols_states.items():  # Splits all columns and fills valid_grid_states with them
#         valid_grid_states[key] = split_col(value)
#     temp_cols = {}  # Temp storage for valid merged cols
#     for key, value in valid_grid_states.items():
#         print key, value
#     if len(valid_grid_states) % 2:
#         for j in range(0, len(valid_grid_states) - 1, 2):
#             print
#             print j, valid_grid_states[j]
#             print j+1, valid_grid_states[j+1]
#             print
#     else:
#         while len(valid_grid_states) > 1:
#             for j in range(0, len(valid_grid_states), 2):
#                 print
#                 print j, valid_grid_states[j]
#                 print j+1, valid_grid_states[j+1]
#                 print
#                 temp_cols[j//2] = compare_cols(valid_grid_states[j], valid_grid_states[j+1])  # Cuts cols down by 1/2
#             valid_grid_states = temp_cols.copy()
#             temp_cols.clear()
#     for key, value in valid_grid_states.items():
#         print key, value
#     return valid_grid_states


def find_valid_grid_states(grid):
    cols_states = find_valid_col_states(grid)
    valid_grid_states = {}  # Storage container for valid grids. Starts as split columns
    for key, value in cols_states.items():  # Splits all columns and fills valid_grid_states with them
        valid_grid_states[key] = split_col(value)
    temp_cols = {}  # Temp storage for valid merged cols
    # for key, value in valid_grid_states.items():
    #     print key, value
    for j in range(len(valid_grid_states)-1):
        valid_grid_states[j+1] = compare_cols(valid_grid_states[j], valid_grid_states[j+1])  # Cuts cols down by 1/2
    # valid_grid_states = temp_cols.copy()
    # temp_cols.clear()
    # print
    # for key, value in valid_grid_states.items():
    #     print key, value
    return valid_grid_states


def answer(grid):
    vld_grd_sts = find_valid_grid_states(grid)
    cnt = 0
    for item in vld_grd_sts[max(vld_grd_sts.keys())].values():
        cnt += len(item)
    return cnt


def generate_binary_arry(height, width):
    random.seed(8675309)
    random.randint(0, 100)
    bin_arry = [[] for i in range(height)]
    for i in range(height):
        for j in range(width):
            bin_arry[i].append(random.randint(0, 100) % 2)
    return bin_arry




class TestExpandingNebula(unittest.TestCase):
    def test1(self):
        test_input = [
                        [True, True, False, True, False, True, False, True, True, False],
                        [True, True, False, False, False, False, True, True, True, False],
                        [True, True, False, False, False, False, False, False, False, True],
                        [False, True, False, False, False, False, True, True, False, False]
                      ]
        self.assertEqual(answer(test_input), 11567)

    def test2(self):
        test_input = [
                        [True, False, True, False, False, True, True, True],
                        [True, False, True, False, False, False, True, False],
                        [True, True, True, False, False, False, True, False],
                        [True, False, True, False, False, False, True, False],
                        [True, False, True, False, False, True, True, True]
                      ]
        self.assertEqual(answer(test_input), 254)

    def test3(self):
        test_input = [
                        [True, False, True],
                        [False, True, False],
                        [True, False, True]
                      ]
        self.assertEqual(answer(test_input), 4)


cell_1 = [[1, 0, 1],
          [0, 1, 0],
          [1, 0, 1]]

cell_2 = [[1, 1]]

cell_3 = [[0],
          [0],
          [0],
          [0],
          [0],
          [0],
          [0],
          [0],
          [0]]



cell_4 = [[1, 1],
          [1, 1]]


zero_arry = []
for i in range(9):
    zero_arry.append([])
    for j in range(20):
        zero_arry[i].append(0)

one_arry = []
for i in range(9):
    one_arry.append([])
    for j in range(25):
        one_arry[i].append(1)

test_arry = generate_binary_arry(9, 10)

st_arry = build_grid_states(cell_2)
st_arry_t = transpose(st_arry)

# for elem in st_arry:
#     for state in st_arry[elem]:
#         print "top: ", state, "bottom: ", st_arry[elem][state]
#     print
#
# vld_col_sts = find_valid_col_states(cell_2)
# print vld_col_sts
# print
# for item in vld_col_sts[0].items():
#         print item[0], "   ---   ", item[1]
#
# vld_row_sts = find_valid_row_states(cell_2)
# cols = compare_cols(vld_col_sts[0], vld_col_sts[1])
# print
# for l, r in cols.items():
#     print "Left: ", l, "   ---   ", "Right: ", r
# print
vld_grd_sts = find_valid_grid_states(one_arry)
cnt = 0
for item in vld_grd_sts[max(vld_grd_sts.keys())].values():
    cnt += len(item)
print (cnt)

if __name__ == '__main__':
    unittest.main()
