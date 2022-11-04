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
    if heights is None or len(heights) == 0 or len(heights[0]) == 0:
        return 0

    rows = len(heights)
    cols = len(heights[0])

    q = []
    visited = set()

    heapq.heappush(q, (0, 0, 0))

    while len(q) > 0:
        effort, row, col = heapq.heappop(q)
        visited.add((row, col))

        if row == rows - 1 and col == cols - 1:
            return effort

        for neighbor in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if neighbor[0] >= 0 and neighbor[0] < rows and neighbor[1] >= 0 and neighbor[1] < cols and neighbor not in visited:
                heapq.heappush(q, (max(effort, abs(heights[row][col] - heights[neighbor[0]][neighbor[1]])), neighbor[0], neighbor[1]))
    
    return None