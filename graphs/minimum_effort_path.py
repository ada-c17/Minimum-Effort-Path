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
    if (heights == None):
        return 0

    nrows = len(heights) # m
    ncols = len(heights[0]) # n
    dirs = [0, 1, 0, -1, 0]

    # diff[i][j] gives max absolute difference to reach (i, j)
    diff = []
    for r in range(0, nrows):
        new_row = []
        for c in range(0, ncols):
            new_row.append(math.inf)
        diff.append(new_row)

    seen = set()

    minHeap = [(0, 0, 0)]  # (d, i, j)
    diff[0][0] = 0

    while minHeap:

      d, i, j = heapq.heappop(minHeap)
      if i == nrows - 1 and j == ncols - 1:
        print(d)
        return d

      seen.add((i, j))
      for k in range(4):
        x = i + dirs[k]
        y = j + dirs[k + 1]
        if x < 0 or x == nrows or y < 0 or y == ncols:
          continue
        if (x, y) in seen:
          continue
        newDiff = abs(heights[i][j] - heights[x][y])
        maxDiff = max(diff[i][j], newDiff)
        if diff[x][y] > maxDiff:
          diff[x][y] = maxDiff
          heapq.heappush(minHeap, (diff[x][y], x, y))
