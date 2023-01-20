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
    cols = len(heights[0])
    visited = set()

    min_eff = 0
    start = [(0, 0, 0)]
    dirs = [(-1, 0), (0, 1), (0, -1), (1, 0)]

    while start:
        eff, row, col = heapq.heappop(start)
        visited.add((row, col))
        min_eff = max(min_eff, eff)

        if row == rows - 1 and col == cols - 1: 
            return min_eff

        for x_coor, y_coor in dirs:
            next_row = row + x_coor
            next_col = col + y_coor

            if rows > next_row >= 0 <= next_col < cols:
                if (next_row, next_col) not in visited:
                    heapq.heappush(start, (abs(heights[row][col] - heights[next_row][next_col]), next_row, next_col))

    return min_eff
