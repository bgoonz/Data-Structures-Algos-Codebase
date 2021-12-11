import itertools


def calculate_graph_distance_matrix(weight_mtx):
    """calculate shortest graph distance matrix"""

    num_vertex = len(weight_mtx)

    dist = [[0 for i in range(num_vertex)] for j in range(num_vertex)]
    for i in range(num_vertex):
        for j in range(num_vertex):
            dist[i][j] = weight_mtx[i][j]

    for k in range(num_vertex):
        for i in range(num_vertex):
            for j in range(num_vertex):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    if dist[j][j] < 0:
                        return -1

    return dist

def calculate_path_length(weight_mtx,path):
    """calculate path length"""

    path_length = 0
    for i in range(len(path)-1):
        path_length += weight_mtx[path[i]][path[i+1]]
    return path_length


def answer(times,time_limit):

    dim = len(times)

    all_paths = [] # all paths from initial point to door
    path_distances = [] # all path with path length

    for i in range(dim-1):
        all_paths.extend(itertools.permutations(range(1,dim-1),i))
    all_paths = [[0] + list(path) + [dim-1] for path in all_paths]


    distance_matrix = calculate_graph_distance_matrix(times)
    if distance_matrix == -1: # if there is a negative cycle
        return range(0,dim-2) # all bunnies can be rescued

    # all possible path that can exit
    for path in all_paths:
        path_len = calculate_path_length(distance_matrix,path)
        if path_len <= time_limit:
            path_distances.append([path,path_len])


    num_rescu = max([len(p[0]) for p in path_distances]) # max number of bunnies can be rescued
    path_distances = [p for p in path_distances if len(p[0]) == num_rescu]

    optimal_paths = [p[0] for p in path_distances]

    for p in optimal_paths:
        p.sort()
    optimal_paths.sort()
    bunny_list = optimal_paths[0][1:-1]
    bunny_list = [i-1 for i in bunny_list]

    return bunny_list
