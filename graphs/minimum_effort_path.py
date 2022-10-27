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
    prev = []
    dist = []
    visited = set()
    q = heapq
    pq = []
    s = 0

    for node in heights:
        prev.append(None)
        dist.append(float('inf'))
    
    if heights:
        q.heappush(pq, (0, s))
        dist[s] = 0

    while len(pq) > 0:
        _, current = q.heappop(pq)
        visited.add(current)
        for neighbor in range(len(heights[current])):
            weight = heights[current][neighbor]
            if weight > 0 and neighbor not in visited:
                temp = dist[current] + weight

                if temp < dist[neighbor]:
                    dist[neighbor] = temp
                    prev[neighbor] = current
                    q.heappush(pq, (dist[neighbor], neighbor))

    res = {
        'previous': prev,
        'distances': dist
    }

    return res

heights = [
    [0, 4, 0, 0],
    [4, 0, 12, 0],
    [0, 12, 0, 0],
    [0,  0, 0, 0]
    ]

print(min_effort_path(heights))

# import heapq

# def min_effort_path(heights):
#     """ Given a 2D array of heights, write a function to return
#         the path with minimum effort.

#         A route's effort is the maximum absolute difference in heights 
#         between two consecutive cells of the route.

#         Parameters
#         ----------
#         heights : list[list[]] (2D array)
#             2D array containing the heights of the available paths

#         Returns
#         -------
#         int
#             minimum effort required to navigate the path from (0, 0) to heights[rows - 1][columns - 1]
#     """
#     dist = []
#     visited = set()
#     q = heapq
#     pq = []
#     length = len(heights[0])
#     height = len(heights)

#     for node in heights:
#         dist.append(float('inf'))
    
#     if heights:
#         q.heappush(pq, (0, 0))
#         dist[0] = 0
#     else:
#         return 0

#     while len(pq) > 0:
#         _, current = q.heappop(pq)
#         for i in range(len(heights)):
#             neighbor = heights[i][current]
#             print('Neighbor: ', neighbor)
#             q.heappush(pq, (dist[i], neighbor))
#         # weight = heights[current][neighbor]
        
#         # if weight > 0:
#         #     temp = dist[current] + weight

#         #     if temp < dist[neighbor]:
#         #         dist[neighbor] = temp
#         # if heights[current].index != -1:
#         #     q.heappush(pq, (dist[neighbor], neighbor))

#     res = dist[-1]
#     return res

# heights = [
#     [1, 2, 2],
#     [3, 8, 2],
#     [5, 3, 5]
# ]

# # heights = [
# #     [1, 2, 3],
# #     [3, 8, 4],
# #     [5, 3, 5]
# # ]

# # heights = [
# #     [1,2,1,1,1],
# #     [1,2,1,2,1],
# #     [1,2,1,2,1],
# #     [1,2,1,2,1],
# #     [1,1,1,2,1]
# # ]

# print(min_effort_path(heights))