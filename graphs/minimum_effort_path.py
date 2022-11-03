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
    # breakthrough: heapq allows you to follow the path with the lowest height diff because you had the difference between each neighbor to the heap, then heappop only takes the lowest diff from the queue. This means if you are following one path, but suddenly that path's difference is greater than a previous difference (difference meaning difference between the height of one node and the previous node), heappop will switch to the other path and then the algorithm will continue from that new node and follow that path
    #
    if heights == None:
        return 0

    rows = len(heights)
    columns = len(heights[0])

    queue = [[0, 0, 0]]
    # diff in height between prev node and new node,
    # x of new node, y of new node
    visited = set()
    directions_to_check = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    # update this as you travese the path with the current lowest difference; max height on minimum effort path
    min_effort = float("-inf")

    while queue:
        # Pop the node with the lowest diff between it and the previous node on the path
        diff, x, y = heapq.heappop(queue)
        # Update the min_effort with the max of either the old max diff or the new diff (the new diff that was pulled from the queue, which should be the next lowest difference between neighboring nodes based on heapq.heappop); it is just updating to the next lowest height difference along the path, but only if that value is greater than previous differences along this min effort path (so it is the max height difference on the min effort path)
        min_effort = max(diff, min_effort)
        if x == rows-1 and y == columns-1:  # if we are at the end of the path!
            return min_effort
        if (x, y) in visited:
            # if not at the end and the coordinate has been visited
            continue  # go to the next coordinate in the queue
        # if have not been here yet, add to visited and keep going
        visited.add((x, y))

        # for each direction you can go from there, determine the dif and the new coordinate
        for x_change, y_change in directions_to_check:
            # locate the next stop along the current path
            new_x = x + x_change
            new_y = y + y_change

            if 0 <= new_x < rows and 0 <= new_y < columns and (new_x, new_y) not in visited:
                # if the coordinates are on the grid and not yet visited
                # find the difference in height between the two cells
                new_diff = abs(heights[x][y]-heights[new_x][new_y])
                # add this as a truple to the queue with the new coordinates
                heapq.heappush(queue, (new_diff, new_x, new_y))
    return -1
