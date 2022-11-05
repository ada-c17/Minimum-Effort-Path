import heapq
import math

def min_effort_path(heights):

    if not heights:
        return 0
    r = len(heights)
    c = len(heights[0])
    diff_matrix = [[math.inf]*c for _ in range(r)]
    diff_matrix[0][0] = 0
    visited = [[False]*c for _ in range(r)]
    queue = [(0, 0, 0)] 
    while queue:
        difference, x, y = heapq.heappop(queue)
        visited[x][y] = True
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            adj_x = x + dx
            adj_y = y + dy
            if 0 <= adj_x < r and 0 <= adj_y < c and not visited[adj_x][adj_y]:
                current_difference = abs(heights[adj_x][adj_y]-heights[x][y])
                max_difference = max(current_difference, diff_matrix[x][y])
                if diff_matrix[adj_x][adj_y] > max_difference:
                    diff_matrix[adj_x][adj_y] = max_difference
                    heapq.heappush(queue, (max_difference, adj_x, adj_y))
    return diff_matrix[-1][-1]
