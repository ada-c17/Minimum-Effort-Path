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
    # Initialize the memoization table
    memo = [[float('inf') for _ in range(columns)] for _ in range(rows)]
    # Base case
    memo[0][0] = 0
    # Initialize the queue
    queue = [(0, 0)]
    # Initialize the directions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # BFS
    while queue:
        row, column = queue.pop(0)
        for direction in directions:
            new_row = row + direction[0]
            new_column = column + direction[1]
            if new_row >= 0 and new_row < rows and new_column >= 0 and new_column < columns:
                effort = max(memo[row][column], abs(heights[row][column] - heights[new_row][new_column]))
                if effort < memo[new_row][new_column]:
                    memo[new_row][new_column] = effort
                    queue.append((new_row, new_column))
    return memo[rows - 1][columns - 1]
