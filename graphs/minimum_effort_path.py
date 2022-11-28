import heapq

class SmartCyclist:
    def __init__(self, arr: list[list[int]]) -> None:
        self.heights = arr
        self.rows = len(arr)
        self.columns = len(arr[0])
        self.min_max_efforts = [[float('inf') for _ in range(self.columns)] for _ in range(self.rows)]
        self.min_max_efforts[0][0] = 0
    
    def enqueue_neighbor(self, priority_queue: list[tuple[int, tuple[int, int]]], current: tuple[int, int], next: tuple[int, int], cur_max_effort: int) -> None:
        cur_row, cur_column = current
        next_row, next_column = next
        max_effort = max(cur_max_effort, abs(self.heights[cur_row][cur_column] - self.heights[next_row][next_column]))
        if max_effort < self.min_max_efforts[next_row][next_column]:
            self.min_max_efforts[next_row][next_column] = max_effort
        heapq.heappush(priority_queue, (self.min_max_efforts[next_row][next_column], (next_row, next_column)))
    
    def calculate_max_effort_along_min_effort_path(self) -> int:
        visited = set()
        pq = []
        heapq.heappush(pq, (0, (0,0)))

        while pq:
            current = heapq.heappop(pq)
            visited.add(current[1])
            (max_effort_to_here, (row, column)) = current
            #up
            if row > 0 and (row - 1, column) not in visited:
                self.enqueue_neighbor(pq, (row, column), (row - 1, column), max_effort_to_here)
            #down
            if row < self.rows - 1 and (row + 1, column) not in visited:
                self.enqueue_neighbor(pq, (row, column), (row + 1, column), max_effort_to_here)
            #left
            if column > 0 and (row, column - 1) not in visited:
                self.enqueue_neighbor(pq, (row, column), (row, column - 1), max_effort_to_here)
            #right
            if column < self.columns - 1 and (row, column + 1) not in visited:
                self.enqueue_neighbor(pq, (row, column), (row, column + 1), max_effort_to_here)
        return self.min_max_efforts[self.rows - 1][self.columns - 1]

    
def min_effort_path(heights: list[list[int]]):
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
    
    sc = SmartCyclist(heights)
    return sc.calculate_max_effort_along_min_effort_path()
