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

    def node_count(row, column, nodes_per_row):
        return row * nodes_per_row + column
    ## make graph
    ## 1  2  3  4 
    ## 5  6  7  8
    ## 9  10 11 12
    heights_y = len(heights)
    heights_x = len(heights[0])
    num_nodes = heights_y * heights_x
    ## graph = [[None for i in range(num_nodes)] for i in range(num_nodes)]
    adj_list = {}
    for i in range(heights_y):
        for j in range(heights_x):
            this_node = node_count(i, j, heights_x)
            adj_list[this_node] = []
            ## above
            if i-1 >= 0:
                ## graph[node_count(i, j, heights_x)][node_count(i-1, j, heights_x)] = abs(heights[i-1][j] - heights[i][j])
                adj_list[this_node].append((node_count(i-1, j, heights_x), abs(heights[i-1][j] - heights[i][j])))
            ## below
            if i+1 < heights_y:
                ## graph[node_count(i, j, heights_x)][node_count(i+1, j, heights_x)] = abs(heights[i+1][j] - heights[i][j])
                adj_list[this_node].append((node_count(i+1, j, heights_x), abs(heights[i+1][j] - heights[i][j])))
            ## left
            if j-1 >= 0:
                ## graph[node_count(i, j, heights_x)][node_count(i, j-1, heights_x)] = abs(heights[i][j-1] - heights[i][j])
                adj_list[this_node].append((node_count(i, j-1, heights_x), abs(heights[i][j-1] - heights[i][j])))
            ## right
            if j+1 < heights_x:
                ## graph[node_count(i, j, heights_x)][node_count(i, j+1, heights_x)] = abs(heights[i][j+1] - heights[i][j])
                adj_list[this_node].append((node_count(i, j+1, heights_x), abs(heights[i][j+1] - heights[i][j])))

    ## print(heights)
    ## print(graph)
    ## print(adj_list)
            
    ## djikstras through graph
    efforts = [float('inf')] * num_nodes

    efforts[0] = 0
    visited = set()
    heap = [(0,0)]

    while heap:
        current = heapq.heappop(heap)[1]
        visited.add(current)
        for i in adj_list[current]:
            node = i[0]
            if node not in visited:
                effort = i[1]
                if effort < efforts[node]:
                    efforts[node] = effort
                heapq.heappush(heap, (efforts[node], node))
    return efforts[-1]
