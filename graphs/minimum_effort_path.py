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

    pq = [(0, (0,0))] # priority queue with the key being the cost of traveling
    costSoFar = {
        (0,0): 0
    } # dictionary of costs to travel to a specific node in the graph. this also serves as a more nuanced visited set

    dirs = [
        (1, 0),     # down
        (0, 1),     # right
        (-1, 0),    # up
        (0, -1)     # left
    ]

    target = (len(heights) - 1, len(heights[0]) - 1) # Early termination condition

    while pq:
        cost, node = heappop(pq) # pop off the node with the lowest cost
        x, y = node
        # early termination of Dijkstra's Algorithm. 
        # Once we've reached the target node, we have already calculated the minimum effort required to travel to it.
        if node == target:
            break
        # travel each direction (down, right, up, left)
        for dir in dirs:
            newX, newY = x + dir[0], y + dir[1]
            # check to make sure we're not going out of bounds
            if newX >= 0 and newX <= len(heights) - 1 and newY >= 0 and newY <= len(heights[0]) - 1:
                myHeight = heights[x][y]
                neighborsHeight = heights[newX][newY]
                cost_between_me_and_neighbor = abs(myHeight - neighborsHeight)
                # important to remember here that the cost of the path is dictated by the 
                # maximum effort required to travel the path. 
                # We set the edge cost to be the max of the path to travel to the neighbor and
                # the effort required to travel to the current node.
                edgeCost = max(cost, cost_between_me_and_neighbor)

                # If neighbor has not been seen before or it has been seen before but we're revisiting via a less costly route
                if (newX, newY) not in costSoFar or ((newX, newY) in costSoFar and edgeCost < costSoFar[(newX, newY)]):
                    costSoFar[(newX, newY)] = edgeCost
                    heappush(pq, (edgeCost, (newX, newY)))

    return costSoFar[target]
