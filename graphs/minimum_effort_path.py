import heapq
from collections import defaultdict
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
    num_rows = len(heights)
    num_cols = len(heights[0])
    distances = defaultdict(lambda: float("inf")) #[['inf']*num_cols]*num_rows
    start = (0,0)
    end = (num_rows-1, num_cols-1)
    distances[start] = 0
    pq = [(distances[start], start)]

    previous = defaultdict(lambda: None)
    visited = set()
    heights_dict = make_dict(heights)
    #dijkstra's
    while pq:
        (min_dist, curr) = heapq.heappop(pq)
        visited.add(curr)
        neighbors = get_neighbors(curr[0], curr[1], heights)
        for neighbor in neighbors:
            if neighbor not in visited:
                diff = abs(heights_dict[curr] - heights_dict[neighbor])
                if diff < distances[neighbor]:
                    previous[neighbor] = curr
                    distances[neighbor] = diff
                heapq.heappush(pq, (distances[neighbor], neighbor))
    #identify path
    path = []
    path.append(end)
    i=0
    while path[-1]!=start:
        path.append(previous[path[i]])
        i+=1
    return distances[max([x for x in path], key=lambda x:distances[x])]

def make_dict(heights):
    heights_dict = {}
    for row in range(len(heights)):
        for col in range(len(heights[row])):
            heights_dict[(row, col)] = heights[row][col]
    return heights_dict

def get_neighbors(r, c, heights):
    neighbors = set({(r, c-1), (r, c+1), (r-1, c), (r+1, c)})
    filtered = [(x,y) for (x,y) in neighbors if x in range(len(heights)) and y in range(len(heights[0]))]
    return filtered
