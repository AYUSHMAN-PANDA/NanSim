import random

def hider_movement(hider_positions, strategic_points, grid_size_x, grid_size_y, grid_margin):
    nearby_offset = 20
    new_positions = []
    for hider in hider_positions:
        prob = random.random()
        # probability of staying with the same strategic point
        if prob <= 0.1:
            new_positions.append(hider)
        # probability of moving to a nearby strategic point
        elif prob <= 0.1 + 0.6:
            nearby_strategic_points = [sp for sp in strategic_points if abs(sp[0] - hider[0]) < nearby_offset and abs(sp[1] - hider[1]) < nearby_offset]
            if nearby_strategic_points:
                new_position = random.choice(nearby_strategic_points)
                new_positions.append(new_position)
            else:
                new_positions.append(hider)
        # probability of moving anywhere else on the grid
        else:
            x = hider[0] + random.choice([-4, -2, 0, 2, 4])
            y = hider[1] + random.choice([-4, -2, 0, 2, 4])
            if(x < grid_margin):
                x = grid_margin
            if(y < grid_margin):
                y = grid_margin
            if(y > grid_margin + grid_size_y):
                y = grid_margin + grid_size_y
            if(x > grid_margin + grid_size_x):
                x = grid_margin + grid_size_x
            new_positions.append((x, y))
    return new_positions
