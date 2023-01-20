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
    # Implement a guard clause/validate the input
    if not heights:
        return 0

    rows = len(heights)
    columns = len(heights[0])
    # Initialize the effort matrix with maximum possible effort
    effort = [[float('inf') for _ in range(columns)] for _ in range(rows)]
    effort[0][0] = 0
    # Initialize the priority queue
    queue = [(0, 0, 0)]
    while queue:
        current_effort, x, y = heapq.heappop(queue)
        # Check if the currentent cell is already visited
        if effort[x][y] < current_effort:
            continue
        # Check the neighbors of the currentent cell
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            # Check if the new cell is within the grid
            if 0 <= new_x < rows and 0 <= new_y < columns:
                new_effort = max(current_effort, abs(heights[new_x][new_y] - heights[x][y]))
                # Check if the new effort is less than the previous effort
                if new_effort < effort[new_x][new_y]:
                    effort[new_x][new_y] = new_effort
                    heapq.heappush(queue, (new_effort, new_x, new_y))
    return effort[rows-1][columns-1]

