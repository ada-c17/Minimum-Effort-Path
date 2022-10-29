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
    # Hint: Use float('inf') to represent infinity
    # Hint: use heapq to implement a priority queue
    if not heights:
        return 0

    max_effort = [[float("inf") for _ in range(len(heights[0]))] for _ in range(
        len(heights))]     

    n_rows = len(heights)
    n_cols = len(heights[0])

    pq = []

    max_effort[0][0] = 0
    # push max_effort_till_now, row, column onto heap    
    heapq.heappush(pq, (0, 0, 0))

    # up, down, forward, backward
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while pq != []:

        max_effort_till_now, row, column = heapq.heappop(pq)
        for i in range(4):          
            new_row = row + directions[i][0]
            new_column = column + directions[i][1]

            # check if new point exists in array
            if new_row >= 0 and new_row < n_rows and new_column >= 0 and new_column < n_cols:

                # if it does, see which is larger, the height difference between the two points, or the current max effort for route
                diff = max(max_effort_till_now, abs(
                    heights[new_row][new_column] - heights[row][column])) 

                # if diff is lower than our current max_effort for that point on array, update max_effort array and add point to queue as we are on the right track
                if diff < max_effort[new_row][new_column]:
                    # set new min difference
                    max_effort[new_row][new_column] = diff
                    # add new point to heap
                    heapq.heappush(pq, (diff, new_row, new_column))

    # target point in the matrix with the required result
    return max_effort[n_rows-1][n_cols - 1]
