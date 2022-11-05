import heapq

def in_bounds(neighbor_inds, n_rows, n_cols):
    if neighbor_inds[0] >= 0 and neighbor_inds[0] < n_rows and neighbor_inds[1] >= 0 and neighbor_inds[1] < n_cols:
        return True
    return False

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
    # guard clause
    if heights == None:
        return 0

    n_rows = len(heights)
    n_cols = len(heights[0])
    
    # make tracking matrix
    heights_diff = [[float('inf') for _ in range(n_cols)] 
                    for _ in range(n_rows)]
    
    # keep track of paths
    visited = set()
    q = [(0, (0, 0))]

    # visit nodes 
    while q: 
        (delta, current) = heapq.heappop(q)
        if current not in visited: 
            visited.add(current)
            # update heights_diff
            heights_diff[current[0]][current[1]] = delta
            
            # add to q
            neighbor_offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for neighbor_offset in neighbor_offsets:
                neighbor_inds = (current[0] + neighbor_offset[0], 
                                current[1] + neighbor_offset[1])
                if in_bounds(neighbor_inds, n_rows, n_cols):
                    diff = abs(heights[neighbor_inds[0]][neighbor_inds[1]] - heights[current[0]][current[1]])
                    if diff > delta:
                        heapq.heappush(q, (diff, neighbor_inds))
                    else: 
                        heapq.heappush(q, (delta, neighbor_inds)) 

    # return min effort
    return heights_diff[-1][-1]