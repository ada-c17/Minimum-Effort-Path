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
    # Get the number of rows and columns
    rows, columns = len(heights), len(heights[0])

    # Initialize the distances array with infinity
    distances = [[float('inf')] * columns for _ in range(rows)]
    pq = []
    
    distances[0][0] = 0
    # Push the starting point into the heap
    heapq.heappush(pq, (0, 0, 0))

    while pq:
        distance, row, column = heapq.heappop(pq)
        if row == rows - 1 and column == columns - 1:
            return distance
        
        # Check the four possible neighbors
        for r, c in ((row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)):
            # Check if the neighbor is within array
            if 0 <= r < rows and 0 <= c < columns:
                # Calculate the new distance
                new_distance = max(distance, abs(heights[r][c] - heights[row][column]))
                if new_distance < distances[r][c]:
                    distances[r][c] = new_distance
                    # Push the new distance into the heap
                    heapq.heappush(pq, (new_distance, r, c))
