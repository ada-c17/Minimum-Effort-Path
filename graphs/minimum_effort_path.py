from heapq import heappush, heappop
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

    pq = [(0,0,0)] # cost, x, y
    row, col = len(heights), len(heights[0])
    visited = set()
    while pq:
        cost,x,y = heappop(pq)
        if (x,y) in visited: continue
        if (x,y) == (row-1,col-1): # reach end of matrix
            return cost
        visited.add((x,y))
        for next_x, next_y in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0 <= x + next_x < row and 0 <= y + next_y < col:
                new_cost = abs(heights[x][y]-heights[x+next_x][y+next_y])
                heappush(pq, (max(cost,new_cost), x + next_x, y + next_y))