import math
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

    h, l = len(heights), len(heights[0])
    efforts = [[math.inf] * l for _ in range(h)]
    efforts[0][0] = 0
    target = (h - 1, l - 1)
    heap = [(0, 0, 0)]

    while heap:
        effort, x, y = heapq.heappop(heap)
        if (x, y) == target:
            return effort
        for row, col in (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y):
            if (row >= 0 and row <= h - 1) and (col >= 0 and col <= l - 1):
                next_effort = max(effort, abs(heights[row][col] - heights[x][y]))
                if efforts[row][col] > next_effort:
                    efforts[row][col] = next_effort
                    heapq.heappush(heap, (next_effort, row, col))
