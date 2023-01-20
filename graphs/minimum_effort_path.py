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

    visited = set() 
    pq = [(0, 0, 0)] 
    
    rows = len(heights)     
    cols = len(heights[0])  

    costs = [[float('inf')] * cols for _ in range(rows)]
    costs[0][0] = 0

    while pq:
        cost, row, col = heapq.heappop(pq)
        
        if (row, col) == (rows-1, cols-1):
            return cost 
        visited.add((row, col))

        neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for node in neighbors:
            neighbor_node = (row + node[0], col + node[1])

            if 0 <= neighbor_node[0] < rows and 0 <= neighbor_node[1] < cols and neighbor_node not in visited:
                new_height = abs(heights[row][col] - heights[neighbor_node[0]][neighbor_node[1]])
                

                if costs[neighbor_node[0]][neighbor_node[1]] > new_height:
                    costs[neighbor_node[0]][neighbor_node[1]] = new_height
                    heapq.heappush(pq, (max(cost, new_height), neighbor_node[0], neighbor_node[1]))
