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

    row = len(heights)
    column = len(heights[0])
    heap = [(0,0,0)]
    effort = 0
    visited = set()

    while heap:
        distance, x, y = heapq.heappop(heap) # pops smallest abs distance (nd)

        effort = max(effort, distance)
        if (x, y) == (row-1, column-1):
            return effort

        visited.add((x, y))

        for nx, ny in (x+1, y), (x-1,y), (x, y+1), (x, y-1):
            if nx >= 0 and nx < row and ny >= 0 and ny < column and (nx, ny) not in visited:
                nd = abs(heights[nx][ny] - heights[x][y])
                heapq.heappush(heap, (nd, nx, ny))

    return effort

# another way to write lines 23 and 24
# row, column = len(heights), len(heights[0])

# Property of heap data structure in Python is that each time the smallest heap element
# is popped(min-heap).
# The heap[0] element also returns the smallest element each time.

# heappop(heap): used to remove and return the smallest element from the heap.
# The order is adjusted, so that heap structure is maintained.

# heappush(heap, ele): used to insert the element mentioned in its arguments into a heap.
# The order is adjusted, so that heap structure is maintained.
