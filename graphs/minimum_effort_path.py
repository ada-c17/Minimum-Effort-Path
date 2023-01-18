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
    rows = len(heights)
    cols = len(heights[0])

    heap = [(0, 0, 0)]  # (effort, row, col)
    dist = [[float('inf') for _ in range(cols)] for _ in range(rows)]
    dist[0][0] = 0
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while heap:
        effort, row, col = heapq.heappop(heap)
        if dist[row][col] < effort:
            continue
        
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols:
                new_effort = max(effort, abs(heights[r][c] - heights[row][col]))
                if new_effort < dist[r][c]:
                    dist[r][c] = new_effort
                    heapq.heappush(heap, (new_effort, r, c))

    return dist[rows-1][cols-1]
