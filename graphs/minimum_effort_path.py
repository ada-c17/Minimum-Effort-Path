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

    effort = [[float("inf") for _ in range(len(heights[0]))] for _ in range(len(heights))]

    nrows = len(heights)
    ncols = len(heights[0])

    pq = []

    effort[0][0] = 0
    heapq.heappush(pq, (0, 0, 0))
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while pq != []:
        effort_till_now, row, col = heapq.heappop(pq)
        for i in range(4):
            new_row = row + directions[i][0]
            new_col = col + directions[i][1]

            if new_row >= 0 and new_row < nrows and new_col >= 0 and new_col < ncols:

                diff = max(effort_till_now, abs(
                    heights[new_row][new_col] - heights[row][col])) 

                if diff < effort[new_row][new_col]:
                    effort[new_row][new_col] = diff
                    heapq.heappush(pq, (diff, new_row, new_col))

    return (effort[nrows-1][ncols - 1])
