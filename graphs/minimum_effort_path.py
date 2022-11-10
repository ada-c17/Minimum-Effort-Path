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
    x = len(heights)
    y = len(heights[0])

    queue = []
    queue.append((0,0))
    visited = {}

    for col in range(y):
        for row in range(x):
            visited[(row,col)] = float('inf')
    visited[(0,0)] = 0
    directions = [[1,0], [0,1], [-1,0], [0,-1]]

    def inside(row, col):
        if 0 <= row < x and 0 <= col < y:
            return True
        return False

    while queue:
        row, col = queue.pop(0)
        currentHeight = heights[row][col]
        currentMax = visited[(row, col)]
        for dRow, dCol in directions:
            newRow = row + dRow
            newCol = col + dCol
            if inside(newRow, newCol):
                neighborHeight = heights[newRow][newCol]
                newMax = max(currentMax, abs(neighborHeight - currentHeight))
                if newMax < visited[(newRow, newCol)]:
                    visited[(newRow, newCol)] = newMax
                    queue.append((newRow, newCol))
    return visited[(x-1, y-1)]


