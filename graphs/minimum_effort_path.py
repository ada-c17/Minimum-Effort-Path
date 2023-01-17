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
    DIR = [0, 1, 0, -1, 0]
    
    def dfs(r, c, visited, threadshold):
        if r == m-1 and c == n-1: 
            return True
        visited[r][c] = True
        for i in range(4):
            nr, nc = r+DIR[i], c+DIR[i+1]
            if nr < 0 or nr == m or nc < 0 or nc == n or visited[nr][nc]: continue
            if abs(heights[nr][nc]-heights[r][c]) <= threadshold and dfs(nr, nc, visited, threadshold): 
                return True
        return False
    
    def can_reach_destination(threadshold):
        visited = [[False] * n for _ in range(m)]
        return dfs(0, 0, visited, threadshold)
    
    left = 0
    result = right = 10**6
    while left <= right:
        mid = left + (right-left) // 2
        if can_reach_destination(mid):
            right = mid - 1
            result = mid
        else:
            left = mid + 1
    return result
