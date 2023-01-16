import heapq

def min_effort_path(heights):
    if  not heights:
        return 0
        
    r,c = len(heights), len(heights[0])
    queue = [(0,0,0)]

    while queue:
        curr = heapq.heappop(queue)
        c_eff =curr[0]
        x = curr[1]
        y = curr[2]

        if x == r-1 and y == c-1:
            return c_eff
        
        if heights[x][y] == '':
            continue

        for dx, dy in [[1,0], [-1,0], [0,1], [0, -1]]:
            newx = x + dx
            newy = y + dy

            if 0 <= newx < r and 0 <= newy < c and heights[newx][newy] != '':
                eff = max(c_eff, abs(heights[newx][newy] - heights[x][y]))
                heapq.heappush(queue, (eff, newx, newy))
        
        heights[x][y] = ''

    matrix = [[2,3,4], [4,9,5], [6,4,6]]
    return matrix

