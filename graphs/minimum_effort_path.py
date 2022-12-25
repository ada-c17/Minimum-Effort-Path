
import heapq

# Time complexity: O(n * m * log(n * m))
# Space complexity: O(n * m)

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
    visited = set()
    r = len(heights)
    c = len(heights[0])
    min_efforts = [[float('inf') for _ in range(c)] for _ in range(r)]
    min_efforts[0][0] = 0
    
    pq = [(0, 0, 0)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while pq:
        effort, i, j = heapq.heappop(pq)
        if (i, j) in visited:
            continue
        visited.add((i, j))
        
        for direction in directions:
            x = i + direction[0]
            y = j + direction[1]
            if 0 <= x < r and 0 <= y < c and (x, y) not in visited:
                max_efforts = max(abs(heights[i][j] - heights[x][y]), effort)
                if max_efforts < min_efforts[x][y]:
                    heapq.heappush(pq, (max_efforts, x, y))
                    min_efforts[x][y] = max_efforts
                    
    return min_efforts[r - 1][c - 1]

