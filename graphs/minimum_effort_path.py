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
    # init variables/direction
    m, n = len(heights), len(heights[0])
    # right, left, up, down
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    # dfs (threshold k) passing in visited
    def dfs(k, x, y):
        visited.add((x, y))

        for dx, dy in dirs:
            new_x, new_y = x+dx, y+dy
            if 0<= new_x<m and 0 <= new_y < n and (new_x, new_y) not in visited:
                new_k = abs(heights[x][y]-heights[new_x][new_y])
                if new_k <= k:
                    dfs(k, new_x, new_y)

    # binary search return max
    mn, mx = -1, max([heights[row][col] for col in range(n) for row in range(m)])
    while mn+1<mx:
        mid = (mn+mx)//2
        visited = set()
        dfs(mid,0,0)
        if (m-1, n-1) in visited:
            mx = mid
        else:
            mn = mid
    
    return mx
