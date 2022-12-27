import heapq
from collections import defaultdict

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
            minimum effort required to navigate the path 
            from (0, 0) to heights[rows - 1][columns - 1]
    
    - need to keep track of effort, row, column
    
    """

    if not heights:
        return 0
    
    rows = len(heights)
    cols = len(heights[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    distances = defaultdict(lambda: float("inf"))
    pqueue = []
    visited = set()

    if heights:
        # (pq, (effort, row, column))
        heapq.heappush(pqueue, (0, 0, 0))
    
    while pqueue:
        # Pop off the node with the least amount of effort
        effort, row, col = heapq.heappop(pqueue)

        target = (rows - 1, cols - 1)
        if (row, col) == target:
            return effort

        visited.add((row, col))

        for x_direction, y_direction in directions: 
            temp_x = row + x_direction
            temp_y = col + y_direction

            if 0 <= temp_x < rows and 0 <= temp_y < cols:
            # Calculate effort 
            # Max absolute difference in heights
                temp_effort = max(effort, abs(heights[temp_x][temp_y] - heights[row][col]))

                if distances[(temp_x, temp_y)] > temp_effort:
                    distances[(temp_x, temp_y)] = temp_effort
                    heapq.heappush(pqueue, (temp_effort, temp_x, temp_y))
