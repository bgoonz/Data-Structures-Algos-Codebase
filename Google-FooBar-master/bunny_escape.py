#BFS from One end to other, along Primary diagonal if possible

from collections import deque

class Vertex:

    def __init__(self, x, y, cap, grd):
        self.x = x
        self.y = y;
        self.cap = cap
        self.grd = grd

    def __hash__(self):
        return self.x ^ self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.cap == other.cap

    def get_neighbors(self):
        neighbors = []
        x = self.x
        y = self.y
        cap = self.cap
        grd = self.grd
        rws = len(grd)
        cols = len(grd[0])

        if x > 0:
            wall = grd[y][x - 1] == 1
            if wall:
                if cap > 0:
                    neighbors.append(Vertex(x - 1, y, cap - 1, grd))
            else:
                neighbors.append(Vertex(x - 1, y, cap, grd))

        if x < cols - 1:
            wall = grd[y][x + 1] == 1
            if wall:
                if cap > 0:
                    neighbors.append(Vertex(x + 1, y, cap - 1, grd))
            else:
                neighbors.append(Vertex(x + 1, y, cap, grd))

        if y > 0:
            wall = grd[y - 1][x] == 1
            if wall:
                if cap > 0:
                    neighbors.append(Vertex(x, y - 1, cap - 1, grd))
            else:
                neighbors.append(Vertex(x, y - 1, cap, grd))

        if y < rws - 1:
            wall = grd[y + 1][x]
            if wall:
                if cap > 0:
                    neighbors.append(Vertex(x, y + 1, cap - 1, grd))
            else:
                neighbors.append(Vertex(x, y + 1, cap, grd))

        return neighbors


class grdEscapeRouter:

    def __init__(self, grd, cap):
        self.grd = grd
        self.rws = len(grd)
        self.cols = len(grd[0])
        self.cap = cap

    def get_escape_route_length(self):
        src = Vertex(0, 0, self.cap, self.grd)
        queue = deque([src])
        dstnc_map = {src: 1}

        while queue:
            current_Vertex = queue.popleft()
            print(current_Vertex.x,current_Vertex.y)

            if current_Vertex.x == self.cols - 1 and current_Vertex.y == self.rws - 1:
                return dstnc_map[current_Vertex]

            for child_Vertex in current_Vertex.get_neighbors():
                if child_Vertex not in dstnc_map.keys():
                    dstnc_map[child_Vertex] = dstnc_map[current_Vertex] + 1
                    queue.append(child_Vertex)

        return 1000 * 1000 * 1000 # Cannot escape

def answer(mat):
    router = grdEscapeRouter(mat,1)
    return router.get_escape_route_length()
