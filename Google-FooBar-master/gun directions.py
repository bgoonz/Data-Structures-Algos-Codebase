import math
import itertools
from fractions import gcd
import time
import bisect


import warnings
warnings.filterwarnings("ignore")

print("\n")

# dimensions = [100,100]
# your_position = [1,2]
# guard_position = [2,2]
# distance = 10000

# dimensions = [3,2]
# your_position = [1,1]
# guard_position = [2,1]
# distance = 4

dimensions = [300,275]
your_position = [150,150]
guard_position = [185,100]
distance = 500


width = dimensions[0];
height = dimensions[1];
A = your_position
B = guard_position;
r = distance;

current_time = time.time()

def distance(p1,p2):
    """return the distance of two points"""
    return math.sqrt( (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 )

def direction(p1,p2):
    """calculate the direction of p1 to p2"""
    p = [p1[0]-p2[0],p1[1]-p2[1]]
    return (p[0]//abs(gcd(p[0],p[1])),p[1]//abs(gcd(p[0],p[1])))

def is_point_allowed(p,directions,distances):
    """test whether shooting to p will hit A first, return True if it will not."""

    # direction and distance
    dirc = p[0]
    dis = p[1]

    # binary search
    index = bisect.bisect_left(directions,dirc)
    if index >= len(directions):
        return True
    elif directions[index] != dirc:
        return True
    else:
        if distances[index] < dis:
            return False
        else:
            return True
        return False


print("1--- %s seconds ---" % (time.time() - current_time))
current_time = time.time()

# all possible mirror points for B
B_mirror_x = list(set([2*n*width + m*B[0] for n in range(-r//width-1, r//width+2) for m in [-1,1]]))
B_mirror_y = list(set([2*n*height + m*B[1] for n in range(-r//height-1, r//height+2) for m in [-1,1]]))
B_mirrors = [(x,y) for x in B_mirror_x for y in B_mirror_y]
B_mirrors = [v for v in B_mirrors if distance(v,A)<=r]

# mirror points for B with unique direction
B_direction_distances = [[direction(v,A),distance(v,A)] for v in B_mirrors]
B_direction_distances.sort()
B_unique_mirrors = [list(grp)[0] for k,grp in itertools.groupby(B_direction_distances,lambda g:g[0])]

# all possible mirror points for A
A_mirror_x = list(set([2*n*width + m*A[0] for n in range(-r//width-1, r//width+2) for m in [-1,1]]))
A_mirror_y = list(set([2*n*height + m*A[1] for n in range(-r//height-1, r//height+2) for m in [-1,1]]))
A_mirrors= [(x,y) for x in A_mirror_x for y in A_mirror_y]
A_mirrors= [v for v in A_mirrors if distance(v,A)<=r and v !=tuple(A)]


# mirror points for A with unique direction
A_direction_distances = [[direction(v,A),distance(v,A)] for v in A_mirrors]
A_direction_distances.sort()
A_unique_mirrors = [list(grp)[0] for k,grp in itertools.groupby(A_direction_distances,lambda g:g[0])]


print("2--- %s seconds ---" % (time.time() - current_time))
current_time = time.time()

# all the directions that can hit A
conflict_directions = list(map(lambda v: v[0],A_unique_mirrors))
conflict_distances = list(map(lambda v: v[1],A_unique_mirrors))

# all the directions that can hit B without hitting A first
B_allowed_directions = [g[0] for g in B_unique_mirrors if is_point_allowed(g,conflict_directions,conflict_distances)]

print("5--- %s seconds ---" % (time.time() - current_time))
current_time = time.time()

print(len(B_allowed_directions))
