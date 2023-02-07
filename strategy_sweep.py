# def diagonal_traversal(n):
#     diagonals = []
#     for k in range(-n + 1, n):
#         diagonal = []
#         for i in range(n):
#             j = k + i
#             if j >= 0 and j < n:
#                 diagonal.append((i, j))
#         diagonals.append(diagonal)
#     return diagonals

# def get_diagonal_elements_topLeft(m, n):
#     '''
#     In this function, the max(m, n) is the number of diagonals in the grid, i and j are the row and column indices of each element 
#     in the diagonal, respectively. The condition if i < m and j < n ensures that the indices are within the grid bounds. 
#     The resulting diagonal_elements list is a list of lists, where each sublist contains the indices of elements in a single diagonal.
#     '''
#     diagonal_elements = []
#     for k in range(max(m, n)):
#         diagonal = []
#         for i in range(k + 1):
#             j = k - i
#             if i < m and j < n:
#                 diagonal.append((i, j))
#         diagonal_elements.append(diagonal)
#     return diagonal_elements

def mirror_image(coordinates):
    res = []
    # print(coordinates)
    for t in coordinates:
        mirrored_coordinates = []
        for x, y in t:
            mirrored_coordinates.append((y, x))
        res.append(mirrored_coordinates)
    return tuple(mirrored_coordinates)

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
    
    # for i in range(grid_margin + m - 1, grid_margin - 1, -1):
    #     diagonal = []
    #     x, y = grid_margin + n-1, i
    #     while x <= grid_margin + m+1 and y >= grid_margin:
    #         diagonal.append((x, y))
    #         x += 1
    #         y -= 1
    #     d2.append(diagonal)
    
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
