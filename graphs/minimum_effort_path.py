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
        
    rows, cols = len(heights), len(heights[0])
    efforts = [[float('inf')] * cols for _ in range(rows)]
    efforts[0][0] = 0
    pq = [(0, 0, 0)]

    while pq:
        effort, r, c = heapq.heappop(pq)
        if (r, c) == (rows - 1, cols - 1):
            return effort
        for nr, nc in (r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c):
            if 0 <= nr < rows and 0 <= nc < cols:
                next_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                if efforts[nr][nc] > next_effort:
                    efforts[nr][nc] = next_effort
                    heapq.heappush(pq, (next_effort, nr, nc))
