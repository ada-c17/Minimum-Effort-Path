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
    
    seen = set()

    n_rows = len(heights)
    n_cols = len(heights[0])

    min_effort = 0
    pq = [(0,0,0)]

    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    while pq != []:

        effort, row, col = heapq.heappop(pq)
        seen.add((n_rows, n_cols))
        min_effort = max(min_effort, effort)

        final= row == n_rows-1 and col == n_cols-1
        if final: 
            return min_effort

        for x, y in directions:
            new_row = row + x
            new_col = col + y
            if n_rows > new_row >= 0 <= new_col < n_cols and (new_row, new_col) not in seen:
                effort = abs(heights[row][col] - heights[new_row][new_col])
                heapq.heappush(pq, (effort, new_row, new_col))

    return min_effort

