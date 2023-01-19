from queue import PriorityQueue

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
    if heights == None:
        return 0
        
    rows = len(heights)
    columns = len(heights[0])

    # Create a 2D array to store the minimum effort required to reach each cell
    effort = [[float('inf') for _ in range(columns)] for _ in range(rows)]

    # Create a priority queue to store the cells to be processed
    q = PriorityQueue()

    # Start with the top-left cell
    effort[0][0] = 0
    q.put((0, 0))

    # Define the possible moves
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while not q.empty():
        # Get the cell with the minimum effort
        row, col = q.get()

        # Check the effort required to move to the neighboring cells
        for dr, dc in moves:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < columns:
                effort_required = max(abs(heights[r][c] - heights[row][col]), effort[row][col])
                if effort_required < effort[r][c]:
                    effort[r][c] = effort_required
                    q.put((r, c))
    return effort[rows-1][columns-1]

# test the function

heights = [[1,2,2],[3,8,2],[5,3,5]]
print(min_effort_path(heights))
