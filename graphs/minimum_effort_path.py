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

    cost = [[float('inf')] * cols for _ in range(rows)]

    pq = []

    cost[0][0] = 0
    heapq.heappush(pq, (0, 0, 0))
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    end = (rows-1, cols-1)

    while pq:
        dist, i, k = heapq.heappop(pq)
        if (i, k) == end:
            return dist

        for x, y in directions: 
            curr_row, curr_col = i+x, k+y 
            if 0 <= curr_row < rows and 0 <= curr_col < cols:
                next_dist = max(dist, abs(heights[curr_row][curr_col] - heights[i][k]))
                if next_dist < cost[curr_row][curr_col]:
                    cost[curr_row][curr_col] = next_dist
                    heapq.heappush(pq, (next_dist, curr_row, curr_col))

# dfs
    # length, height = len(heights), len(heights[0])

    # neighbors = [[1,0],[0,1],[-1,0],[0,-1]]

    # def dfs(shortest_path, x, y):
    #     visited.add((x, y))

    #     for n_x, n_y in neighbors: 
    #         if 0 <= n_x + x < length and 0 <= n_y + y < height and (n_x + x, n_y + y) not in visited: 
    #             if abs(heights[x][y] - heights[n_x + x][n_y + y]) <= shortest_path: 
    #                 dfs(shortest_path, n_x + x, n_y + y)

    # first, last = -1, max(max(heights, key=max))

    # while first + 1 < last: 
    #     mid = (first + last)//2
    #     visited = set()

    #     dfs(mid, 0, 0)
        
    #     if (length - 1, height - 1) in visited: 
    #         last = mid 
    #     else: 
    #         first = mid 

    # print(last)
    # return last
