import heapq
def min_effort_path(heights):
    if not heights: 
        return 0

    rows = len(heights)
    columns = len(heights[0])
    min_effort = 0
    queue = [(0,0,0)]
    visited = set()

    while queue:
        effort, row, col = heapq.heappop(queue)
        visited.add((row, col))
        min_effort = max(min_effort, effort)
        if row == rows - 1 and col == columns - 1:
            return min_effort
        
        for x, y in [(0,1), (0, -1), (1,0), (-1, 0)]:
            new_row = row + x
            new_col = col + y
            if rows > new_row >= 0 <= new_col < columns and (new_row, new_col) not in visited:
                effort = abs(heights[row][col] - heights[new_row][new_col])
                heapq.heappush(queue, (effort, new_row, new_col))
    return min_effort

