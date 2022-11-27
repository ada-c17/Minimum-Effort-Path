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

    rows, columns = len(heights), len(heights[0])
    distances = [[float("inf")] * columns for row in range(rows)]

    # starting node is set to 0
    distances[0][0] = 0

    # queue of nodes to be visited
    priority_queue = [(0, 0, 0)] #  (distance, row, column)

    # record of all visted nodes
    visited = set()

    while priority_queue:
        distance, row, column = heapq.heappop(priority_queue)

        # if the queue is the last node, return the shortest distance
        if (row, column) == (rows - 1, columns - 1):
            return distance

        visited.add((row, column))

        neighbors = [(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)]

        for neighbor in neighbors:
            neighbor_row, neighbor_column = neighbor
            if (0 <= neighbor_row < rows and 0 <= neighbor_column < columns) and neighbor not in visited:
                new_distance = max(distance, abs(heights[row][column] - heights[neighbor_row][neighbor_column]))
                if distances[neighbor_row][neighbor_column] > new_distance:
                    distances[neighbor_row][neighbor_column] = new_distance
                    heapq.heappush(priority_queue, (max(distance, new_distance), neighbor_row, neighbor_column))
