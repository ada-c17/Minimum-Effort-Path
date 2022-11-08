import math
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
    grid = heights

    if not grid:
        return 0
        
    h = [(0, (0,0))] 
    costSoFar = {(0,0): 0}

    dirs = [(1,0), (0,1), (-1,0), (0,-1)] 
    trgt = (len(grid)-1, len(grid[0])-1) 

    while h:
        cost, node = heappop(h)
        x, y = node
        if node == trgt:
            break
        for dir in dirs:
            newX, newY = x+dir[0], y+dir[1]

            if newX >= 0 and newX <= len(grid)-1 and newY >= 0 and newY <= len(grid[0])-1:
                edgeCost = max(cost, abs(grid[x][y] - grid[newX][newY])) 
                if (newX, newY) not in costSoFar or ( (newX, newY) in costSoFar and edgeCost < costSoFar[(newX, newY)]):
                    costSoFar[(newX, newY)] = edgeCost
                    heappush(h, (edgeCost, (newX, newY)))
                    
    return costSoFar[trgt]