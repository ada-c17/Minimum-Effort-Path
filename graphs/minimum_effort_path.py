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
    cols = len(heights[0])
    pq = [(0,0,0)] # (effort, row, col)
    min_effort = 0
    visited = set()

    while pq:
        effort, row, col = heapq.heappop(pq)
        min_effort = max(min_effort, effort)
        if (row, col) == (rows-1, cols-1):
            return min_effort
        visited.add((row, col))

        for new_x, new_y in (row+1, col), (row-1, col), (row, col+1), (row, col-1):
            if 0 <= new_x < rows and 0 <= new_y < cols and (new_x, new_y) not in visited:
                curr_effort = abs(heights[new_x][new_y] - heights[row][col])
                heapq.heappush(pq, (curr_effort, new_x, new_y))
    return min_effort