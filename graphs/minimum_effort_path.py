import heapq
from heapq import heappush, heappop

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

    m, n = len(heights), len(heights[0])

    # to be able to go in all directions
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    output = 0
    pq = [(0,0,0)]
    visited = set()

    while pq: 
        path, row , col = heappop(pq)
        output = max(output, path)
        if (row, col) == (m-1, n-1):
            return output
        visited.add((row, col))
        for rows, cols in directions:
            new_row, new_col = row+rows, col+cols
            if 0<=new_row<m and 0<=new_col<n and (new_row, new_col) not in visited:
                new_path = abs(heights[row][col]-heights[new_row][new_col])
                heappush(pq,(new_path, new_row, new_col))
    

