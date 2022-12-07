import heapq as hq

def min_effort_path(heights):
    """ Given a 2D array of heights, write a function to return
        the path with minimum effort.

        A route's effort is the maximum absolute difference in heights 
        between two consecutive cells of the route.

        Parameters
        ----------
        heights : list[list[]] (2D array)
            2D array containing the heights of the available paths

        Returns
        -------
        int
            minimum effort required to navigate the path from (0, 0) to heights[rows - 1][columns - 1]

        Pseudocode
        ----------
        Create current to store index
        Create effort list equal to rows * columns to store effort from start
        Create previous list equal to rows*columns to store prev node
        Create visited set
        Create queue
    """
    if not heights:
        return 0
    current = None
    queue = []
    visited = set()
    moves = [(0, -1), (-1, 0), (1, 0), (0,1)]
    hq.heappush(queue, (heights[0][0], (0, 0)))
    efforts = [([float('inf')] * len(heights[0])) for i in heights]
    efforts[0][0] = 0
    while queue:
        current = hq.heappop(queue)
        visited.add(current[1])
        neighbors = {(heights[neighbor[0]][neighbor[1]], neighbor) for move in moves
            if (neighbor:=tuple(abs(x+y) for x, y in zip(current[1], move))) not in visited
            and neighbor[0]<len(heights) and neighbor[1]<len(heights[0])}
        for neighbor in neighbors:
            if neighbor not in visited:
                x, y = current[1]
                a, b = neighbor[1]
                neighbor_effort = abs(heights[x][y] - neighbor[0])
                if neighbor_effort < efforts[a][b]:
                    efforts[a][b] = neighbor_effort
                hq.heappush(queue, (efforts[a][b], (a, b)))

    return efforts[-1][-1]
    