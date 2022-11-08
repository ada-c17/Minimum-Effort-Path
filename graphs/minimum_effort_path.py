import heapq

def min_effort_path(heights):
    """ Given a 2D array of heights, write a function to return
        the path with minimum effort.

        A route's effort is the maximum absolute difference in heights 
        between two consecutive cells of the route.

        Parameters
        ----------
        heights : list[list[]] (2D array)ake
            2D array containing the heights of the available paths

        Returns
        -------
        int
            minimum effort required to navigate the path from (0, 0) to heights[rows - 1][columns - 1]
    """
    # create a dictionary to store the coordinants and cost ie {(0,0):0}
    # create a priority queue to retain first element and self coordinate (0,(0,0))
    # use djestra but with absolute value in difference instead of sum
    # store minimum effort path
    # need length of all elements in heights
    # need length of all elements in one of the arrays
    # start (0,0) top left
    # end heights[-1][-1] bottom right - base case
    if heights:
        rows, columns = len(heights), len(heights[0])
        visited = set()

        # cost = {():int}
        min_efforts = [[float('inf')] * columns for _ in range(rows)]
        min_efforts[0][0] = 0
        
        pq = [(0,0,0)] # minimum effort, row, and column of current cell

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while pq: 
            minimum, i, j = heapq.heappop(pq)
            visited.add((i,j))

            for d in directions:
                new_i = i + d[0]
                new_j = j + d[1]
                if 0 <= new_i < rows and 0 <= new_j < columns and (new_i, new_j) not in visited:
                    max_effort = max(abs(heights[i][j]-heights[new_i][new_j]), minimum)

                    if max_effort <  min_efforts[new_i][new_j]:
                        heapq.heappush(pq, (max_effort, new_i, new_j))
                        min_efforts[new_i][new_j] = max_effort
        return min_efforts[-1][-1]
    else:
        return 0


    # for node in heights:
    #     cost.append(float('inf'))
    #     previous.append(None)
    # if heights:
    #     heapq.heappush(pq,(0,heights[0][0]))
    #     cost = {heights[0][0]: 0}


