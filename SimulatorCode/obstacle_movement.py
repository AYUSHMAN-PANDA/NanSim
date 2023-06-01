import random

def move_obstacle(obstacle_positions, grid_size_x, grid_size_y, grid_margin):
    new_obstacle_positions = []
    for obstacle in obstacle_positions:
        x, y = obstacle
        new_x = x + random.choice([-4, 0, 4])
        new_y = y + random.choice([-4, 0, 4])
        if new_x >= grid_margin and new_x < grid_size_x + grid_margin and new_y >= grid_margin and new_y < grid_size_y+grid_margin:
            new_obstacle_positions.append((new_x, new_y))
        else:
            new_obstacle_positions.append(obstacle)
    return new_obstacle_positions