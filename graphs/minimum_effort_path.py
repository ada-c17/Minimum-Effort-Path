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

    efforts = []
    for _ in range(len(heights)):
        efforts.append([float('inf')] * len(heights[0]))
    efforts[0][0] = 0

    visited = []
    for _ in range(len(heights)):
        visited.append([False] * len(heights[0]))

    queue = []
    heapq.heappush(queue, (0, (0, 0)))

    while queue:
        _, (row, col) = heapq.heappop(queue)
        visited[row][col] = True
        neighbors = get_neighbors(row, col, heights, visited)
        for neighbor in neighbors:
            n_row, n_col = neighbor
            effort = max(abs(heights[row][col] - heights[n_row]
                         [n_col]), efforts[row][col])
            if effort < efforts[n_row][n_col]:
                efforts[n_row][n_col] = effort
            heapq.heappush(queue, (efforts[n_row][n_col], (n_row, n_col)))

    return efforts[len(heights)-1][len(heights[0])-1]


def get_neighbors(row, col, heights, visited):
    possible_neighbors = [(row - 1, col), (row + 1, col),
                          (row, col - 1), (row, col + 1)]
    neighbors = []
    for neighbor in possible_neighbors:
        n_row, n_col = neighbor
        if 0 <= n_row < len(heights) and 0 <= n_col < len(heights[0]) and not visited[n_row][n_col]:
            neighbors.append(neighbor)
    return neighbors
