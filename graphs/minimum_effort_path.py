import heapq
import math

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

    m, n = len(heights), len(heights[0])
    dist = [[math.inf] * n for _ in range(m)]
    dist[0][0] = 0
    minHeap = [(0, 0, 0)] # distance, row, col
    DIR = [0, 1, 0, -1, 0]

    while minHeap:
        d, r, c = heapq.heappop(minHeap)
        if d > dist[r][c]: continue
        if r == m - 1 and c == n - 1:
            return d
        
        for i in range(4):
            nr, nc = r + DIR[i], c + DIR[i+1]
            if 0 <= nr < m and 0 <= nc < n:
                newDist = max(d, abs(heights[nr][nc] - heights[r][c]))
                if dist[nr][nc] > newDist:
                    dist[nr][nc] = newDist
                    heapq.heappush(minHeap, (dist[nr][nc], nr, nc))
