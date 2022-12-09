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

    r,c = len(heights), len(heights[0])
    q = [(0,0,0)]
    effort = 0
    visited =set()
    
    while q:
        d, x, y = heapq.heappop(q)
        print(d,x,y)
        moves = [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]
        effort = max(d, effort)
        print(f"this is the effort: {effort}")
        if (x,y) == (r-1, c-1):
            return effort
        visited.add((x,y))
        for row, column in moves:
            if row >= 0 and row < r and column >= 0 and column < c and (row, column) not in visited:
                new_effort = abs(heights[row][column]- heights[x][y])
                heapq.heappush(q,(new_effort,row,column))

    return effort



