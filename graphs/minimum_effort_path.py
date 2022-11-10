from heapq import heappop
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
    visited = set()
    minEffort = 0
    minHeap = [(0, 0, 0)] # distance, row, col
    directions = [(0, 1),(1, 0), (-1,0), (0,-1)]

    while minHeap:
        dis, row, col = heappop(minHeap)
        visited.add((row,col))
        minEffort = max(minEffort, dis)
        # hit bottom of 2d array
        if row == rows - 1 and col == cols - 1:
            return minEffort  
        for moveToX, moveToY in directions:
            nextRow = row + moveToX
            nextCol = col + moveToY
            if rows > nextRow >= 0 <= nextCol < cols and (nextRow, nextCol) not in visited:
                heapq.heappush(minHeap, (abs(heights[row][col] - heights[nextRow][nextCol]), nextRow, nextCol))

    return minEffort