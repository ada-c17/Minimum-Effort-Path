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

    visited = set() # holds coords of visited cells
    pq = [(0, 0, 0)] # (cost, row, col)
    
    # coordinates for last cell, and bounds of heights matrix
    rows = len(heights)     
    cols = len(heights[0])  

    costs = [[float('inf')] * cols for _ in range(rows)]
    costs[0][0] = 0

    while pq:
        cost, row, col = heapq.heappop(pq)
        # at the end of the path, return the lowest cost
        if (row, col) == (rows-1, cols-1):
            return cost 
        visited.add((row, col))
        #              up      right   down    left
        neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # for loop to visit other possible neighbor nodes
        for node in neighbors:
            # calculate neighbor position
            neighbor_node = (row + node[0], col + node[1])
            # if it's within bounds of heights
            if 0 <= neighbor_node[0] < rows and 0 <= neighbor_node[1] < cols and neighbor_node not in visited:
                # height difference between current cell and neighbor cell
                new_height = abs(heights[row][col] - heights[neighbor_node[0]][neighbor_node[1]])
                # only adjust height in costs and add to pq if it's lower?
                # this part helps make it faster (according to leetcode)
                if costs[neighbor_node[0]][neighbor_node[1]] > new_height:
                    costs[neighbor_node[0]][neighbor_node[1]] = new_height
                    heapq.heappush(pq, (max(cost, new_height), neighbor_node[0], neighbor_node[1]))
