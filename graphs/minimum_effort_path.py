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
    if heights == None:
        return 0

    rows = len(heights)
    cols = len(heights[0])
    visited = set()
    minimum_effort = 0
    pq = [(0, 0, 0)] # heap (effort, row, col)
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    while pq:
        effort, row, col = heapq.heappop(pq)
        visited.add((row, col))
        minimum_effort = max(minimum_effort, effort)

        target= row == rows-1 and col == cols-1
        if target: 
            return minimum_effort
        #BFS
        for cord_x, cord_y in dirs:
            next_row = row + cord_x
            next_col = col + cord_y
            if rows > next_row >= 0 <= next_col < cols and (next_row, next_col) not in visited:
                effort = abs(heights[row][col] - heights[next_row][next_col])
                heapq.heappush(pq, (effort, next_row, next_col))

    return minimum_effort

    #priorque-key of cost travelling, use abs value 
    #initialize the pq , first element is the amount of effort to travel to that cell, the second element is the cell's coordinates(tuple)
    # while pq:
    # pop the cost and the current_node off the queue using heappop
    # target = (len(heights - 1), len(heights[0]) - 1)
    # in our loop for the pq we can say if the node we are at == target then we can break out of the loop
    # current_node is going to hold the coordinates for the node we're currently looking at so you can assign curr_x, curr_y using the curr_node

    # then you can use the list of the different directions we can go
