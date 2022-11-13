import math
import heapq

def min_effort_path(heights):
    
    if not heights:
        return 0

    rows, cols = len(heights), len(heights[0])

    difference_matrix = [[math.inf]* cols for i in range(rows)]
    difference_matrix[0][0] = 0 

    visited = [[False]* cols for i in range(rows)]

    queue = [(0,0,0)] # difference, x, y
    while queue:
        diff, x, y = heapq.heappop(queue)
        visited[x][y] = True
        for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
            adjacent_x = x + dx
            adjacent_y = y + dy
            if 0 <= adjacent_x < rows and 0 <= adjacent_y < cols and not visited[adjacent_x][adjacent_y]:
                current_diff = abs(heights[adjacent_x][adjacent_y] - heights[x][y])
                max_difference = max(current_diff, difference_matrix[x][y])
                if difference_matrix[adjacent_x][adjacent_y] > max_difference:
                    difference_matrix[adjacent_x][adjacent_y] = max_difference
                    heapq.heappush(queue, (max_difference, adjacent_x, adjacent_y))
    return difference_matrix[-1][-1]

    
