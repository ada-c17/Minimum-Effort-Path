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
        
    rows = len(heights)
    columns = len(heights[0])
    
    pq = [[0,0,0]]  ##diff,x,y
    
    visited = set()
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    ans = float('-inf')
    
    while pq:
        diff,x,y=heapq.heappop(pq)
        ans=max(diff,ans)
        if x==rows-1 and y==columns-1:
            return ans
        
        if (x,y) in visited:
            continue
        
        visited.add((x,y))
        
        for dx,dy in directions:
            new_x = x+dx
            new_y = y+dy
            
            if new_x>=0 and new_x<rows and new_y>=0 and new_y<columns and (new_x,new_y) not in visited:
                diff = abs(heights[x][y]-heights[new_x][new_y])
                heapq.heappush(pq,(diff,new_x,new_y))
    
    return -1             