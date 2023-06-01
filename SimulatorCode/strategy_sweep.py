def get_diagonal_elements(m, n, grid_margin):
    d1 = []
    d2 = []
    d3 = []
    d4 = []
    for i in range(grid_margin + m - 1, grid_margin - 1, -1):
        diagonal = []
        x, y = i, grid_margin + n-1
        while x <= grid_margin + m+1 and y >= grid_margin:
            diagonal.append((x, y))
            x += 1
            y -= 1
        d1.append(diagonal)
        
    for j in range(grid_margin + n - 1, grid_margin - 1, -1):
        diagonal = []
        x, y = j, grid_margin
        while x >= grid_margin and y <= grid_margin +  n + 1:
            diagonal.append((x, y))
            x -= 1
            y += 1
        d2.append(diagonal)

    for i in range(grid_margin + m - 1, grid_margin - 1, -1):
        diagonal = []
        x, y = i, grid_margin + n - 1
        while x >= grid_margin and y >= grid_margin:
            diagonal.append((x, y))
            x -= 1
            y -= 1
        d3.append(diagonal)

    for j in range(grid_margin + n - 1, grid_margin -1, -1):
        diagonal = []
        x, y = grid_margin + m - 1, j
        while x >= grid_margin and y >= grid_margin:
            diagonal.append((x, y))
            x -= 1
            y -= 1
        if (len(diagonal) == 0):
            break
        d4.append(diagonal)

    return [d1, d2, d3, d4]
