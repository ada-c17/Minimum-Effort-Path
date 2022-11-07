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
    if len(heights) == 0:
        return 0
    visited = set()
    m = len(heights)
    n = len(heights[0])
    min_efforts = [[float("inf")] * n for _ in range(m)]
    min_efforts[0][0] = 0
    # heapq store current min effort, index of row i, and index of col j
    pq = [(0, 0, 0)]
    # set direction to find neighbor left, down, up, and right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while pq:
        cur_min_effort, i, j = heapq.heappop(pq)
        visited.add((i, j))

        for d in directions:
            next_i = i + d[0]
            next_j = j + d[1]
            if 0 <= next_i < m and 0 <= next_j < n and (next_i, next_j) not in visited:
                new_min_efforts = max(abs(heights[i][j] - heights[next_i][next_j]), cur_min_effort)
                if new_min_efforts < min_efforts[next_i][next_j]:
                    min_efforts[next_i][next_j] = new_min_efforts
                    heapq.heappush(pq, (new_min_efforts, next_i, next_j))
    return min_efforts[-1][-1]


