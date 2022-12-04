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

    # init pq of tuples [(travel cost, (x,y coord))] 
    pq = [(0, (0,0))]

    # init dict of visited/costs to travel to spec cell in graph
    travel_costs = {
        (0,0): 0
        }

    nav = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
    ]

    # set coord of bottom right cell to terminate early
    target = (len(heights) - 1, len(heights[0]) - 1)

    while pq:
        cost, node = heappop(pq)
        x, y = node

        if node == target:
            break
        
        for coord in nav:
            neighbor_x, neighbor_y = x + coord[0], y + coord[1]

            if neighbor_x >= 0 and neighbor_x <= len(heights) - 1 and neighbor_y >= 0 and neighbor_y <= len(heights[0]) - 1:
                curr_height = heights[x][y]
                neighbor_height = heights[neighbor_x][neighbor_y]
                cost_neighbor_curr = abs(curr_height - neighbor_height)

                edgecost = max(cost, cost_neighbor_curr)
            
            # if neighbor not in visited or neighbor is in visited & edgecost < cost(neighbor)
                if (neighbor_x, neighbor_y) not in travel_costs or ((neighbor_x, neighbor_y) in travel_costs and edgecost < travel_costs[(neighbor_x, neighbor_y)]):
                    travel_costs[(neighbor_x, neighbor_y)] = edgecost
                    heappush(pq, (edgecost, (neighbor_x, neighbor_y)))

    return travel_costs[target]