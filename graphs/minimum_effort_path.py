import heapq

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
    """
    if not heights:
        return 0
    
    rows = len(heights)
    columns = len(heights[0])

    # initialize costs
    min_max_efforts = [[float('inf') for _ in range(columns)] for _ in range(rows)]
    min_max_efforts[0][0] = 0

    visited = set()
    pq = []
    heapq.heappush(pq, (0, (0,0)))

    while pq:
        current = heapq.heappop(pq)
        visited.add(current[1])
        (max_effort_to_here, (row, column)) = current
        #up
        if row > 0 and (row - 1, column) not in visited:
            visit_neighbor(heights, min_max_efforts, pq, row, column, row - 1, column, max_effort_to_here)
        #down
        if row < rows - 1 and (row + 1, column) not in visited:
            visit_neighbor(heights, min_max_efforts, pq, row, column, row + 1, column, max_effort_to_here)
        #left
        if column > 0 and (row, column - 1) not in visited:
            visit_neighbor(heights, min_max_efforts, pq, row, column, row, column - 1, max_effort_to_here)
        #right
        if column < columns - 1 and (row, column + 1) not in visited:
            visit_neighbor(heights, min_max_efforts, pq, row, column, row, column + 1, max_effort_to_here)
    return min_max_efforts[rows - 1][columns - 1]

def visit_neighbor(heights, min_max_efforts, pq, prev_row, prev_column, next_row, next_column, max_effort_to_here):
    max_effort = max(max_effort_to_here, abs(heights[prev_row][prev_column] - heights[next_row][next_column]))
    if max_effort < min_max_efforts[next_row][next_column]:
        min_max_efforts[next_row][next_column] = max_effort
    heapq.heappush(pq, (min_max_efforts[next_row][next_column], (next_row, next_column)))