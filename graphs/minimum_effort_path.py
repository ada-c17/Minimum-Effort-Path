from collections import deque
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
    pass
    if heights == None:
        return 0
    H = len(heights)
    W = len(heights[0])
    
    directions = [[1,0], [0,1], [-1,0], [0,-1]]
    def inside(row, col):
        return 0 <= row < H and 0 <= col < W
    if len(heights) >0:

        queue = deque([])
        queue.append((0, 0))
    
        cost = { (row, col): float('inf') for col in range(W) for row in range(H) }
        cost[(0, 0)] = 0
    
    while queue:
        row, col = queue.popleft()
        current_height = heights[row][col]
        current_cost = cost[(row, col)]
        for d_row, d_col in directions:
            new_row = row + d_row
            new_col = col + d_col
            if inside(new_row, new_col):
                neighbor_height = heights[new_row][new_col]
                new_cost = max(current_cost, abs(neighbor_height - current_height))
                if new_cost < cost[(new_row, new_col)]:
                    cost[(new_row, new_col)] = new_cost
                    queue.append((new_row, new_col))
    
    return cost[(H - 1, W - 1)]

