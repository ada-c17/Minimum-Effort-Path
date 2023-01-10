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

    max_effort = [[float("inf") for _ in range(len(heights[0]))] for _ in range(
        len(heights))]

    n_num_of_rows = len(heights)
    n_num_of_cols = len(heights[0])

    pq = []

    max_effort[0][0] = 0
    heapq.heappush(pq, (0, 0, 0))
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while pq != []:
        max_effort_till_now, row, col = heapq.heappop(pq)
        for i in range(4):
            new_row = row + directions[i][0]
            new_col = col + directions[i][1]

            if new_row >= 0 and new_row < n_num_of_rows and new_col >= 0 and new_col < n_num_of_cols:

                diff = max(max_effort_till_now, abs(
                    heights[new_row][new_col] - heights[row][col])) 

                if diff < max_effort[new_row][new_col]:
                    max_effort[new_row][new_col] = diff
                    heapq.heappush(pq, (diff, new_row, new_col))

    return (max_effort[n_num_of_rows-1][n_num_of_cols - 1])
