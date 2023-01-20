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
    # heights: list of lists
    if not heights:
        return 0

    num_rows = len(heights)
    num_cols = len(heights[0])    

    queue = []
    heapq.heappush(queue, (0, 0, 0))

    visited = set()
    min_effort = 0

    while queue:
        current_effort, row, col = heapq.heappop(queue)
        min_effort = max(min_effort, current_effort)
        visited.add((row, col))

        if row == num_rows - 1 and col == num_cols - 1:
            return min_effort

        for x, y in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if x >= 0 and x < num_rows and y >= 0 and y < num_cols and (x, y) not in visited:
                new_effort = abs(heights[row][col] - heights[x][y])
                heapq.heappush(queue, (new_effort, x, y))

    return min_effort            
