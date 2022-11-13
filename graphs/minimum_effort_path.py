def min_effort_path(heights):
    if not heights:
        return 0
    
    h = len(heights)
    w = len(heights[0])
    queue = []
    queue.append((0,0))
    seen = {}

    for c in range(w):
        for r in range(h):
            seen[(r,c)] = float('inf')
    seen[(0,0)] = 0
    directions = [[1,0], [0,1], [-1,0], [0,-1]]

    def inner(r, c):
        if 0 <= r < h and 0 <= c < w:
            return True
        return False

    while queue:
        r, c = queue.pop(0)
        currentH = heights[r][c]
        currentM = seen[(r, c)]
        for dR, dC in directions:
            newR = r + dR
            newC = c + dC
            if inner(newR, newC):
                neighborH = heights[newR][newC]
                newM = max(currentM, abs(neighborH - currentH))
                if newM < seen[(newR, newC)]:
                    seen[(newR, newC)] = newM
                    queue.append((newR, newC))
    return seen[(h-1, w-1)]


