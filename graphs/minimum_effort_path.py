from heapq import heappush, heappop

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

    pq = [(0, (0,0))]
    costs = {
        (0,0): 0
        }
    target = (len(heights) - 1, len(heights[0]) - 1)

    directions = [
        (1, 0),     # down
        (0, 1),     # right
        (-1, 0),    # up
        (0, -1)     # left
    ]

    while pq:
        cost, node = heappop(pq)
        x, y = node

        if node == target:
            break

        for direction in directions:
            new_x, new_y = x + direction[0], y + direction[1]
            
            if new_x >= 0 and new_x <= len(heights) - 1 and new_y >= 0 and new_y <= len(heights[0]) - 1:
                current_height = heights[x][y]
                neighbors_height = heights[new_x][new_y]
                cost_between = abs(current_height - neighbors_height)

                edge_cost = max(cost, cost_between)

                if (new_x, new_y) not in costs or ((new_x, new_y) in costs and edge_cost < costs[(new_x, new_y)]):
                    costs[(new_x, new_y)] = edge_cost
                    heappush(pq, (edge_cost, (new_x, new_y)))

    return costs[target]



