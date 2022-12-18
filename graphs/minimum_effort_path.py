import heapq

def min_effort_path(heights):
    """ 
    Given a 2D array of heights, write a function to return
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
    """
    #----------------------HINT-----------------------
    # A modified version of Dijkstra may be used here where the effort is the difference between two heights, 
    # as opposed to the cumulation of the edge cost between nodes.
    if not heights:
        return 0
    
    x_max = len(heights) 
    y_max = len(heights[0]) 
    directions = [(0,1), (0,-1), (-1,0), (1,0)]
    
    efforts = [[float('inf')] * y_max for i in range(x_max)]

    efforts[0][0] = 0

    pq = []

    # First value is height diff(aka effort), last two are x and y coord respectively
    heapq.heappush(pq, (0,0,0))
    while pq:
        effort, x, y = heapq.heappop(pq)

        if x == x_max - 1 and y == y_max - 1:
            return effort

        for dir in directions:
            new_x = x + dir[0]
            new_y = y + dir[1]

            if 0 <= new_x < x_max and 0 <= new_y < y_max:
                new_effort = max(abs(heights[new_x][new_y] - heights[x][y]), effort)

                if new_effort < efforts[new_x][new_y]:
                    efforts[new_x][new_y] = new_effort
                    heapq.heappush(pq, (new_effort, new_x, new_y))


