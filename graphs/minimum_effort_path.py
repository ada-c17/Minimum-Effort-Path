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
    
    - need to keep track of effort, row, column
    
    """

    if not heights:
        return 0
    
    rows = len(heights)
    cols = len(heights[0])

    pqueue = []
    visited = set()

    if heights:
        heapq.heappush(pqueue, (0, 0, 0))
    
    while pqueue:
        # Pop off the node with the least amount of effort
        effort, row, col = heapq.heappop(pqueue)
        visited.add((row, col))

        # Loop through the row in the graph?
        # Calculate effort 
        # Max absolute difference in heights
        # Left, right, up, down
        # for neighbor in range(cols):
        #     if 

