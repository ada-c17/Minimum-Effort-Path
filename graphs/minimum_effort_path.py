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
    dist = 0
    current = 0
    visited = set()

    if not heights:
        return 0

    if len(heights) > 1:
        visited.add(current)
    else:
        return 0
    
    for nodes in heights:
        for neighbor in range(1, len(heights)):
            weight = heights[neighbor][current] - heights[neighbor - 1][current]
            if weight > 0 and neighbor not in visited:
                if (neighbor == 1 and current == 0) or weight < dist:
                    dist = weight
        current += 1
    return dist
    

heights = [
    [1, 2, 2],
    [3, 8, 2],
    [5, 3, 5]
] # Expecting: 2
print(min_effort_path(heights))

heights = [
    [1, 2, 3],
    [3, 8, 4],
    [5, 3, 5]
] # Expecting: 1
print(min_effort_path(heights))

heights = [
    [1,2,1,1,1],
    [1,2,1,2,1],
    [1,2,1,2,1],
    [1,2,1,2,1],
    [1,1,1,2,1]
] # Expecting: 0
print(min_effort_path(heights))

heights = [
    [1,2,1,1,1,1],
    [1,2,1,2,1,2],
    [1,2,1,2,1,3],
    [1,2,1,2,1,3],
    [1,1,1,2,1,2]] # Expecting: 1
print(min_effort_path(heights))