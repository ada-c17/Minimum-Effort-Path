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
    if heights is None: 
        return 0 

    # set target to last elem in array 
    max_x = len(heights)-1
    max_y = len(heights[0])-1
    target = (max_x, max_y)

    # initialize queue to check each node in input 
    priority_queue = [(0, (0,0))]

    #initialize distance: track distance from start -> each node 
    distance = {
        # from 0,0 to itself = 0 
        (0,0): 0 
    }

    directions = [
    (1, 0), #down   
    (0, 1), # right 
    (-1, 0), # up
    (0, -1) #left 
    ]

    while priority_queue: 
        # in each iteration, remove first elem 
        cost, node = heappop(priority_queue)
        # set current node to first in priority_queue 
        current_x, current_y = node 

        if node == target: 
            break 


        for direction in directions: 
            # loop through directions to check neighbors (when valid)
            # find the shortest distance from current_node to neighbors
            new_x, new_y = current_x + direction[0], current_y + direction[1]
            if max_x >= new_x >= 0 <= new_y <= max_y: 
                # current node 
                current_node = heights[current_x][current_y]
                # each valid neighbor for current 
                current_neighbor = heights[new_x][new_y]


                # get abs val of distance between current node and neighbor
                # in each directiion (by looping through directions)
                distance_between = abs(current_node - current_neighbor) 
                edge_cost = max(cost, distance_between)


                if (new_x, new_y) not in distance or ((new_x, new_y) in distance 
                and edge_cost < distance[new_x, new_y]):
                    #find the best edge_cost between current node and 
                    # next node in all valid directions, add that to distance dict 
                    distance[(new_x, new_y)] = edge_cost 
                    print(distance)
                    # push new coordinates to check in all directions 
                    heappush(priority_queue, (edge_cost, (new_x, new_y)))
    # print(distance)
    return distance[target]


# heights = [
#     [1,2,2],
#     [3,8,2],
#     [5,3,5]]

# min_effort_path(heights)

