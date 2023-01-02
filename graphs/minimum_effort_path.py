import heapq

def min_effort_path(heights):
    """Given a 2D array of heights, write a function to return
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
    # heap is comprised of (effort, row, column)
    heap = []
    heapq.heappush(heap, (0, (0,0)))
    visited = set()
    while heap:
        node = heapq.heappop(heap)
        effort = node[0]
        r = node[1][0]
        c = node[1][1]
        visited.add((r, c))
        if r == len(heights) - 1 and c == len(heights[0]) - 1:
            return effort
        
        for neighbor in get_valid_neighbor_coordinates(r, c, heights):
            if neighbor != None:
                this_effort = max(effort, abs(heights[r][c] - heights[neighbor[0]][neighbor[1]]))
                if neighbor not in visited or this_effort < effort:
                    heapq.heappush(heap, (this_effort, (neighbor[0], neighbor[1])))
    
    return None
        

def get_valid_neighbor_coordinates(r, c, heights):
    '''
    returns valid neighbor cordinates
    '''
    top_neighbor, right_neighbor, bottom_neighbor, left_neighbor = None, None, None, None
    if r > 0:
        top_neighbor_r = r - 1
        top_neighbor = (top_neighbor_r, c)
    if r < len(heights) - 1:
        bottom_neighbor_r = r + 1
        bottom_neighbor = (bottom_neighbor_r, c)
    if c > 0:
        left_neighbor_c = c - 1
        left_neighbor = (r, left_neighbor_c)
    if c < len(heights[0]) - 1:
        right_neighbor_c = c + 1
        right_neighbor = (r, right_neighbor_c)

    return [top_neighbor, right_neighbor, bottom_neighbor, left_neighbor]
