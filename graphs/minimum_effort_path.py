from heapq import *
def is_valid_index(heights, index):
    if index < 0 or index >= len(heights):
        return False
    else:
        return True

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
   #create a list to store the shortest paths
    distances = {}
    #create a set to store nodes already visited
    visited = set()

    #create an empty priority queue
    pq = []

    #initialize each node in distances to infinity
    for i in range(len(heights)):
        for j in range(len(heights[i])):
            distances[(i,j)] = float('inf')

    #if the graph is not empty
    if heights:
        #Add the start node to the priority queue
        heappush(pq, (0, (0,0)))
        
        #Set the distance of the start node to itself to zero
        distances[(0,0)] = 0

    #while the priority queue is not empty
    while len(pq) > 0:
        #pop the minimum node off of the priority queue
        #_ is the distance to the minimum node, current is the node's index
        cost_to_travel, coordinate = heappop(pq)
        cur_x, cur_y = coordinate
        #add current to visited
        visited.add(coordinate)
        #loop through current's neighbors
        #note since g is an adjacency matrix, we are actually looping through all nodes here
        # we will find the actual neighbors inside the for loop
        neighbors = []
        if is_valid_index(heights[0], cur_y - 1):
            up = (cur_x, cur_y -1)
            neighbors.append(up)
        if is_valid_index(heights[0], cur_y + 1):
            down = (cur_x,cur_y +1)
            neighbors.append(down)
        if is_valid_index(heights, cur_x - 1):
            left = (cur_x -1,cur_y)
            neighbors.append(left)
        if is_valid_index(heights, cur_x + 1):
            right = (cur_x +1,cur_y)
            neighbors.append(right)
        for neighbor_coord in neighbors:
            neighbor_x, neighbor_y = neighbor_coord

            #get the weight of the edge from current -> neighbor
            edge_weight = abs(heights[cur_x][cur_y] - heights[neighbor_x][neighbor_y]) 
            #if there is actually an edge between current & neighbor
            #and the neighbor has not yet been visited
            if edge_weight > 0 and neighbor_coord not in visited:
                #calculate the cost of path from start node -> neighbor via current node
                if distances[coordinate] != float('inf'):
                    temp_distance = max(distances[coordinate], edge_weight)
                else:
                    temp_distance = edge_weight
                #if calculated distance is less than current listed distance for neighbor
                if temp_distance < distances[neighbor_coord]:
                    #set new minimum distance to temp_distance
                    distances[neighbor_coord] = temp_distance
                    #add neighbor to priority queue setting its distance as its priority
                    heappush(pq, (temp_distance, neighbor_coord))
    final_cell = (len(heights) -1, len(heights)-1)
    print(distances[final_cell])
    maximum = 0
    for coordinate, distance in distances.items():
        if distance > maximum:
            maximum = distance
    return maximum