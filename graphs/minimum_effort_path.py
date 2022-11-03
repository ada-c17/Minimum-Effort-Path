
import heapq

#HELPER FUNCTION
def valid_next_moves(position, grid, visited):

    # moves-> TUPLE which holds each possible move, given a current position
    # position-> a TUPLE in which position[0] is ROW index and position[1] is COLUMN index-> see its use as helper function below
    possible_moves = (
        (position[0] + 1, position[1]),  # down
        (position[0] - 1, position[1]),  # up
        (position[0], position[1] + 1),  # right
        (position[0], position[1] - 1),  # left
    )

    # data structure to hold possible moves to return to caller of helper function
    valid_moves = []

    # Iterate over each move
    for row, column in possible_moves:
        # Check 2 things-> if move within grid and move's position has not been visited
        if (0 <= row < len(grid) 
            and 0 <= column < len(grid[0])
            and (row, column) not in visited):
            # Append to valid moves
                valid_moves.append((row, column))

    return valid_moves

#MAIN FUNCTION
def min_effort_path(heights):

    if not heights:
        return 0
    
    # Set to hold all (row, column) positions/spots visited
    visited = set()
    
    # Heap to hold (row, column) positions to visit
    heap = []

    # priority of cue is min_max_effort-> none yet, so set to 0. Position is second argument. Heaps can hold multiple args, not like queues
    heapq.heappush(heap, (0, (0,0)))

    result = 0

    while heap:
        # pop off lowest priority 
        min_max_effort, position = heapq.heappop(heap)

        # keep track of min, max_effort diff in a path-> and Dijkstra's will take you there first?
        result = max(result, min_max_effort)

        if position == (len(heights)-1, len(heights[0])-1):
                return result

        # Must be OUTSIDE OF FOR LOOP? B/c this is NOT FIFO structure-> it's a priority queue?
        visited.add(position)

        # Find all possible next moves
        moves = valid_next_moves(position, heights, visited)
        for move in moves:
            #get current effort -> effort from current position to the move
            current_min_max_effort = abs(heights[move[0]][move[1]] - heights[position[0]][position[1]])

            heapq.heappush(heap, (current_min_max_effort, move))
