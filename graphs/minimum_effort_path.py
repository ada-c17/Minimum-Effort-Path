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
    vis = [[False for i in range(cols)] for j in range(rows)]
    q = []
    heapq.heappush(q, (0,0,0))
    while len(q) > 0:
        cur = heapq.heappop(q)
        if vis[cur[1]][cur[2]]:
            continue
        if cur[1] == rows-1 and cur[2] == cols-1:
            return cur[0]
        vis[cur[1]][cur[2]] = True
        for row, col in [(-1,0),(1,0),(0,-1),(0,1)]:
            next_row, next_col = cur[1]+row, cur[2]+col
            if 0<=next_row<rows and 0<=next_col<cols and not vis[next_row][next_col]:
                heapq.heappush(q, (max(cur[0], abs(heights[next_row][next_col]-heights[cur[1]][cur[2]])), next_row, next_col))
    return -1

heights = [[1,2,2],[3,8,2],[5,3,5]]
print(min_effort_path(heights))