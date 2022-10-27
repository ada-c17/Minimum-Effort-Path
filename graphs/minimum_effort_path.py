from distutils.ccompiler import new_compiler
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
    if not heights: return 0

    num_rows = len(heights)
    num_cols = len(heights[0])

    efforts = [[float('inf')] * num_cols for _ in range(num_rows)]
    efforts[0][0] = 0

    queue = [(0, 0, 0)]
    visited = set()

    while len(queue) > 0:
        _, row, col = heapq.heappop(queue)
        visited.add((row, col))

        neighbors = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1),
        ]

        for (n_row, n_col) in neighbors:
            if not (0 <= n_row < num_rows) or not (0 <= n_col < num_cols):
                continue
            if (n_row, n_col) in visited:
                continue

            effort = max(abs(heights[row][col] - heights[n_row][n_col]), efforts[row][col])

            if effort < efforts[n_row][n_col]:
                efforts[n_row][n_col] = effort

            heapq.heappush(queue, (effort, n_row, n_col))

    return efforts[-1][-1]