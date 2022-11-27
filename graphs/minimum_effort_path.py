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

    if not heights:
        return 0
    
    rows = len(heights)
    cols = len(heights[0])
    maps = {i: dict() for i in range(rows * cols)}
    for r in range(rows):
        for c in range(cols):
            if r != 0:
                maps[r * cols + c][(r - 1) * cols + c] = abs(heights[r][c] - heights[r - 1][c])
            if r < rows - 1:
                maps[r * cols + c][(r + 1) * cols + c] = abs(heights[r][c] - heights[r + 1][c])
            if c != 0:
                maps[r * cols + c][r * cols + (c - 1)] = abs(heights[r][c] - heights[r][c - 1])
            if c < cols - 1:
                maps[r * cols + c][r * cols + (c + 1)] = abs(heights[r][c] - heights[r][c + 1])
    
    prev = [None for i in range(rows * cols)]
    abs_dists = [float('inf') for i in range(rows * cols)]
    visited = set()
    pq = []
    heapq.heapify(pq)
    heapq.heappush(pq, (0, 0))

    while pq:
        cur_abs_dist, cur_node = heapq.heappop(pq)
        visited.add(cur_node)
        for neighbor, abs_dist in maps[cur_node].items():
            if neighbor not in visited:
                abs_dists[neighbor] = max(abs_dist, cur_abs_dist)
                heapq.heappush(pq, (abs_dists[neighbor], neighbor))
                prev[neighbor] = cur_node

    return abs_dists[cols * rows - 1]

    
# THINGS THAT DIDN'T WORK LOL
    # cur = 0
    # dest = cols - 1
    # min_effort = float("inf")
    # while cur != dest:
    #     for neighbor, effort in maps[cur].items():
    #         min_effort = min(effort, min_effort)

#     return dfs(0, (rows * cols) - 1, maps, float("-inf"))

# def dfs(cur, dest, maps, max_effort, visited=None):
#     if not visited:
#         visited = set()
#     min_effort = float("inf")
#     if cur == dest:
#         return max_effort
#     visited.add(cur)
#     for neighbor, effort in maps[cur].items():
#         print(max_effort, effort)
#         if neighbor not in visited:
#             cur_max_effort = dfs(neighbor, dest, maps, max(max_effort, effort), visited)
#             min_effort = min(cur_max_effort, min_effort)
#     return min_effort
