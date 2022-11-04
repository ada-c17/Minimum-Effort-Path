import heapq

# Notes/references:
# Used https://replit.com/@adadev/graphs-p2-practice-1#dijkstra/cheapest_flight.py


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
    
    visited = {}
    dest = (len(heights)-1, len(heights[0]) -1)

    for i in range(len(heights)):
        for j in range(len(heights[i])):
            visited[(i,j)] = False

    # Initialize a priority queue
    pq = []

    # Queue tuple: 1st item max effort so far, 2nd item is height, 3rd item is cell coordinates
    # Add the first element to the queue 
    heapq.heappush(pq, (0, heights[0][0], (0,0)))

    while pq:

        # Pop the min_effort cell off the queue
        current_effort, height, current_cell = heapq.heappop(pq)

        # if cell = dest, it means we reached the final cell and popped off the path to get there that had the smallest max effort
        if current_cell == dest:
            return current_effort
        
        visited[current_cell] = True
        neighbors = []

        # Add left neighbor
        if current_cell[1] != 0:
            neighbors.append((current_cell[0], current_cell[1] - 1))

        # Add right neighbor
        if current_cell[1] != len(heights[0]) - 1:
            neighbors.append((current_cell[0], current_cell[1] + 1))

        # Add up neighbor
        if current_cell[0] != 0:
            neighbors.append((current_cell[0] - 1, current_cell[1]))

        # Add down neighbor
        if current_cell[0] != len(heights) - 1:
            neighbors.append((current_cell[0] + 1, current_cell[1]))

        # Loop through the neighbor cells and add them to the PQ if not visited
        # Eventually, the dest will be a neighbor cell and get added to the PQ
        for cell in neighbors:
            if not visited[cell]:
                new_height = heights[cell[0]][cell[1]]
                new_effort = abs(new_height - height)
                effort_to_append = new_effort if new_effort > current_effort else current_effort
                heapq.heappush(pq, (effort_to_append, new_height, cell))

