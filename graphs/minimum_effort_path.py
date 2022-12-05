import math
from queue import Queue
from typing import List
from collections import deque
from typing import List
import heapq
from heapq import heappop, heapify
from heapq import heappush


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

        time complexity: O(rows * columns * log(rows * columns)) because heappop uses log of rows * columns
        space complexity: of O(rows * columns)


    """
    if not heights:
        return 0

    rows, cols = len(heights), len(heights[0])
    visited = set()
    min_heap = [(0, (0, 0))]

    while min_heap:
        weight, (row, col) = heapq.heappop(min_heap)

        # exit if we got to the end
        if (row, col) == (rows - 1, cols - 1):
            return weight

        # down, up, right, left
        directions = (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)

        for next_row, next_col in directions:
            if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
                continue
            if (next_row, next_col) in visited:
                continue

            new_weight = abs(heights[row][col] - heights[next_row][next_col])
            heapq.heappush(min_heap, (new_weight, (next_row, next_col)))

        visited.add((row, col))

    return -1
