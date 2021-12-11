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

def compare_cols(col_1, col_2):
    valid_col_states = {}
    for key, value in col_1.items():
        for elem in value:  # Checks for all cols of first col
            for key_2 in col_2.keys():  # Checks if right col of 1st col state is same as left col of 2nd col state
                if elem == key_2[0]:
                    valid_col_states[(key[:] + (elem,) + key_2[1:])] = col_2[key_2]
    return valid_col_states


def find_valid_grid_states(grid):
    cols_states = find_valid_col_states(grid)
    valid_grid_states = {}  # Storage container for valid grids. Starts as split columns
    for key, value in cols_states.items():  # Splits all columns and fills valid_grid_states with them
        valid_grid_states[key] = split_col(value)
    temp_cols = {}  # Temp storage for valid merged cols

    for j in range(len(valid_grid_states)-1):
        valid_grid_states[j+1] = compare_cols(valid_grid_states[j], valid_grid_states[j+1])  # Cuts cols down by 1/2

    return valid_grid_states


def answer(grid):
    if len(grid[0])<len(grid):
        grid =  list(map(list, zip(*grid)))

    vld_grd_sts = find_valid_grid_states(grid)
    cnt = 0
    for item in vld_grd_sts[max(vld_grd_sts.keys())].values():
        cnt += len(item)
    return cnt


'''
>>> answer([[True,False,True],[False,True,False],[True,False,True]])
4
>>> answer([[True,False,True]])
8
>>> answer([[True]])
4
>>> answer([[False]])
12
>>> 
'''
