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
    
    rows, columns = len(heights), len(heights[0])

    distances = [[float("inf")] * columns for row in range(rows)]

    distances[0][0] = 0
    priority_queue = [(0, 0, 0)]
    visited = set()

    while priority_queue:
        dist, row, col = heapq.heappop(priority_queue)
        if (row, col) == (rows-1, columns -1):
            return dist
        visited.add((row, col))
        neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for neighbor in neighbors:
            neighbor_row, neighbor_col = neighbor
            if (0 <= neighbor_row < rows and 0 <=neighbor_col < columns) and neighbor not in visited:
                 new_dist = max(dist, abs(heights[row][col] - heights[neighbor_row][neighbor_col]))
                 if distances[neighbor_row][neighbor_col] > new_dist:
                    distances[neighbor_row][neighbor_col] = new_dist
                    heapq.heappush(priority_queue, (max(dist, new_dist), neighbor_row, neighbor_col))
