def min_effort_path(heights):
    '''
    constrains: 1 <= heights[i][j] <= 10^6, difference between 0-10^6 sorted value 
    using Binary Search approach to check effort < mid or > mid to reduce time
    '''
    if not heights:
        return 0

    row = len(heights)
    col = len(heights[0])

    def boolBfsBinarySearch(mid):
        visited = [[False]*col for _ in range(row)]
        queue = [(0, 0)]  
        while queue:
            x, y = queue.pop()
            #base case: reached the destination cell with minimum effort value
            if x == row-1 and y == col-1:
                return True
            visited[x][y] = True
            for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nei_r = x + dr
                nei_c = y + dc
                if 0 <= nei_r < row and 0 <= nei_c < col and not visited[nei_r][nei_c]:
                    compare = abs(heights[nei_r][nei_c]-heights[x][y])
                    #binary search between 0 and 10^6
                    if compare <= mid:
                        visited[nei_r][nei_c] = True
                        queue.append((nei_r, nei_c))

    left = 0
    right = 10**6
    while left < right:
        mid = (left + right)//2
        if boolBfsBinarySearch(mid):
            right = mid
        else:
            left = mid + 1
    return left
