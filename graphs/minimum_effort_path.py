
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
    if not heights or not heights[0]:
        return 0
    rows = len(heights)
    columns = len(heights[0])
    dp = [[float("inf") for _ in range(columns)] for _ in range(rows)]
    dp[0][0] = 0
    for i in range(rows):
        for j in range(columns):
            if i - 1 >= 0:
                dp[i][j] = min(dp[i][j], max(dp[i-1][j], abs(heights[i][j]-heights[i-1][j])))
            if j - 1 >= 0:
                dp[i][j] = min(dp[i][j], max(dp[i][j-1], abs(heights[i][j]-heights[i][j-1])))
    return dp[-1][-1]
