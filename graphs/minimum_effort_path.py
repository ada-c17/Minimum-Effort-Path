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

    visited = [[False for _ in range(columns)] for _ in range(rows)]
    effort = [[float('inf') for _ in range(columns)] for _ in range(rows)]

    effort[0][0] = 0
    heap = [(0, 0, 0)]

    while heap:
        curr_effort, row, col = heapq.heappop(heap)

        if visited[row][col]:
            continue

        visited[row][col] = True

        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < rows and 0 <= c < columns:
                new_effort = max(curr_effort, abs(heights[row][col] - heights[r][c]))

                if new_effort < effort[r][c]:
                    effort[r][c] = new_effort
                    heapq.heappush(heap, (new_effort, r, c))

    return effort[rows-1][columns-1]
