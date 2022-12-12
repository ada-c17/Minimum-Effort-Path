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

    rows, cols = len(heights), len(heights[0])
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    min_path = 0
    priority_queue = [(0,0,0)]
    visited = set()

    while priority_queue: 
        cost, row, col = heapq.heappop(priority_queue)
        min_path = max(min_path, cost)
        if (row, col) == (rows - 1, cols - 1):
            return min_path

        visited.add((row, col))

        for direction_x, direction_y in directions:
            new_row, new_col = row + direction_x, col + direction_y
            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                new_path = abs(heights[row][col] - heights[new_row][new_col])
                heapq.heappush(priority_queue, (new_path, new_row, new_col))
