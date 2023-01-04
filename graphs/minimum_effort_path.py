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

    rows = len(heights)
    columns = len(heights[0])
    queue = []
    heapq.heappush(queue, (0, 0, 0))
    visited = set()
    max_diff = 0
    
    while queue:
        cost, row, col = heapq.heappop(queue)
        max_diff = max(max_diff, cost)
        if (row, col) in visited:
            continue
        visited.add((row, col))
        if row == rows - 1 and col == columns - 1:
            return max_diff
        
        for r, c in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if r >= 0 and r < rows and c >= 0 and c < columns and (r, c) not in visited:
                new_diff = abs(heights[row][col] - heights[r][c])
                heapq.heappush(queue, (new_diff, r, c))
                
    return max_diff

