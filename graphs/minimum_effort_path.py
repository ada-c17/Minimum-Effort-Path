from collections import defaultdict
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
    graph = defaultdict(list)
    if not heights:
        return 0
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    rows = len(heights)
    cols = len(heights[0])

    for x in range(cols):
        for y in range(rows):
            for direction in directions:
                newx, newy = x + direction[0], y + direction[1]
                if newx >= 0 and newx < cols and newy >= 0 and newy < rows:
                    abs_difference = abs(heights[y][x] - heights[newy][newx])
                    graph[(y,x)].append(((newy, newx), abs_difference))
    visited = set()
    min_heap = []
    start = (0,0)
    end = (rows-1, cols-1)
    min_heap.append((0, start))
    max_abs = 0
    while min_heap:
        cost_till, curr, = heapq.heappop(min_heap)
        visited.add(curr)
        max_abs = max(max_abs, cost_till)
        if curr == end:
            return max_abs
        for next, to_reach in graph[curr]:
            if next not in visited:
                heapq.heappush(min_heap, (to_reach, next))
    return max_abs
