import heapq
def min_effort_path(heights):
    if not heights:
        return 0

    efforts = []
    for _ in range(len(heights)):
        row = []
        for _ in range(len(heights[0])):
            row.append(float('inf'))
        efforts.append(row)
    efforts[0][0] = 0

    visited = []
    for _ in range(len(heights)):
        row = []
        for _ in range(len(heights[0])):
            row.append(False)
        visited.append(row)

    queue = []
    heapq.heappush(queue, (0, (0, 0)))

    while queue:
        priority, (row, col) = heapq.heappop(queue)
        visited[row][col] = True
        neighbors = get_neighbors(row, col, heights, visited)
        for neighbor in neighbors:
            n_row, n_col = neighbor
            effort = max(abs(heights[row][col] - heights[n_row]
                        [n_col]), efforts[row][col])
            if effort < efforts[n_row][n_col]:
                efforts[n_row][n_col] = effort
            heapq.heappush(queue, (efforts[n_row][n_col], (n_row, n_col)))

    return efforts[len(heights)-1][len(heights[0])-1]


def get_neighbors(row, col, heights, visited):
    potential_neighbors = [(row - 1, col), (row + 1, col),
                        (row, col - 1), (row, col + 1)]
    neighbors = []
    for neighbor in potential_neighbors:
        n_row, n_col = neighbor
        if 0 <= n_row < len(heights) and 0 <= n_col < len(heights[0]) and not visited[n_row][n_col]:
            neighbors.append(neighbor)
    return neighbors
        
    

