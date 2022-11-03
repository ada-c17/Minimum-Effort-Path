from cmath import inf
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

    #dictionary of costs for each position
    costs = {(0,0):0}
    # priority queue
    pq = [(0, (0,0))]

    final = (len(heights) - 1, len(heights[0]) - 1)

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while pq:
        cost, node = heappop(pq)
        x, y = node
        if node == final:
            break

        for direction in directions:
            newX, newY = x + direction[0], y + direction[1]
            if 0 <= newX <= final[0] and 0 <= newY <= final[1]:
                currentHeight = heights[x][y]
                neighborsHeight = heights[newX][newY]
                costBetweenNeighborAndCurrent = abs(currentHeight - neighborsHeight)
                edgeCost = max(cost, costBetweenNeighborAndCurrent)
                
                if (newX, newY) not in costs or edgeCost < costs[(newX, newY)]:
                    costs[(newX, newY)] = edgeCost
                    heappush(pq, (edgeCost, (newX, newY)))

    return costs[final]