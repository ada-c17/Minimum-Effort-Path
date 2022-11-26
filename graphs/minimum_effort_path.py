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

    rows, columns = len(heights),len(heights[0])
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = set()
    pq = [(0,0,0)]

    while pq:
        effort, r, c = heapq.heappop(pq)
        visited.add((r,c))
        if r == rows-1 and c == columns-1:
            return effort
        for dr, dc in directions:
            new_r, new_c = r+dr, c+dc
            if 0 <= new_r < rows and 0 <= new_c < columns and (new_r,new_c) not in visited:
                new_effort = abs(heights[r][c] - heights[new_r][new_c])
                heapq.heappush(pq, (new_effort, new_r, new_c))
    return -1