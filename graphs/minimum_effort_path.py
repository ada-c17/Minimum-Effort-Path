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
    minHeap = [(0, 0, 0)]
    visited = set()
    effort = 0

    while minHeap:
        difference, x, y = heapq.heappop(minHeap)
        moves = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]
        effort = max(effort, difference)
        
        if (x, y) == (rows - 1, cols - 1):
            return effort
        visited.add((x, y))
        for row, col in moves:
            if row >= 0 and row < rows and col >= 0 and col < cols and (row, col) not in visited:
                new_effort = abs(heights[row][col] - heights[x][y])
                heapq.heappush(minHeap, (new_effort, row, col))
            
    return effort
        # if r == rows - 1 and c == cols - 1:
        #     return result
        
        # visited.add((r, c))

        # for row, col in [(r + 1, c), (r - 1, c)], (r, c - 1), (r, c + 1)]:
        #     if row >= 0 and row <rows and col >= 0 and col < cols and (row,col) not in visited:
        #         newDifference = abs(heights[r][c] - heights[row][col])
        #         heapq.heappush(minHeap, (newDifference, row,))

            


    # directions = [(1,0), (-1, 0), (0,1), (0,-1)]
