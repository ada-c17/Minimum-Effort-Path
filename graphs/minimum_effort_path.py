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

    pq = [(0, (0,0))] 
    costSoFar = {
        (0,0): 0
    } 
    dirs = [
        (1, 0),    
        (0, 1),     
        (-1, 0),    
        (0, -1)     
    ]

    target = (len(heights) - 1, len(heights[0]) - 1)

    while pq:
        cost, node = heappop(pq) 
        x, y = node
        
        if node == target:
            break
        for dir in dirs:
            newX, newY = x + dir[0], y + dir[1]

            if newX >= 0 and newX <= len(heights) - 1 and newY >= 0 and newY <= len(heights[0]) - 1:
                myHeight = heights[x][y]
                neighborsHeight = heights[newX][newY]
                cost_between_me_and_neighbor = abs(myHeight - neighborsHeight)
                edgeCost = max(cost, cost_between_me_and_neighbor)

                if (newX, newY) not in costSoFar or ((newX, newY) in costSoFar and edgeCost < costSoFar[(newX, newY)]):
                    costSoFar[(newX, newY)] = edgeCost
                    heappush(pq, (edgeCost, (newX, newY)))

    return costSoFar[target]
