from random import randint, choice, shuffle
import reference_data as ref

def get_new_world(size=64):
    world = {
        'grid': [list([0] * size) for x in xrange(size)],
        'size': size
    }
    world['grid'] = generate_terrain(world['grid'])
    
    return world
    
    
# Key: g=grassland, w=woodland, r=rockland
# TODO: Speed up by changing jump to any empty tile
#       that has same adjacent OR chance to skip jump?
def generate_terrain(grid):
    size = len(grid)
    empty_tiles = range(0, size*size)
    tiles_remaining = size*size
    terrain_table = {}
    for terrain_type in ref.terrain_dct.keys():
        terrain_table[terrain_type] = None
    starting_points = []
    test_point = (randint(0, size-1), randint(0, size-1))
    while len(starting_points) < len(terrain_table.keys()):
        while test_point not in starting_points:
            starting_points.append(test_point)
            test_point = (randint(0, size-1), randint(0, size-1))
    for terrain_type in terrain_table.keys():
        terrain_table[terrain_type] = starting_points[0]
        starting_points = starting_points[1:]
    for terrain_type in terrain_table.keys():
        t = terrain_table[terrain_type]
        grid[t[0]][t[1]] = terrain_type
        empty_tiles.remove(t[0]*size + t[1])
    tiles_remaining -= len(terrain_table.keys())

    while tiles_remaining > 0:
        for terrain_type in terrain_table.keys():
            checked_tiles = 0
            t = terrain_table[terrain_type]
            adjacents = [(t[0] - 1, t[1]),
                         (t[0] + 1, t[1]),
                         (t[0], t[1] - 1),
                         (t[0], t[1] + 1)]
            shuffle(adjacents)
            for next_t in adjacents:
                x = next_t[0]
                y = next_t[1]
                if x < 0 or x >= size or y < 0 or y >= size:
                    checked_tiles += 1
                    if checked_tiles == 4:
                        jump = (randint(0, size-1), randint(0, size-1))
                        jumped_to = grid[jump[0]][jump[1]]
                        if jumped_to in [0, t]: 
                            terrain_table[terrain_type] = jump
                    continue    
                if grid[next_t[0]][next_t[1]] == 0:
                    grid[next_t[0]][next_t[1]] = terrain_type
                    empty_tiles.remove(next_t[0]*size + next_t[1])
                    terrain_table[terrain_type] = next_t
                    tiles_remaining -= 1
                else:
                    checked_tiles += 1
                    if checked_tiles == 4:
                        jump = (randint(0, size-1), randint(0, size-1))
                        jumped_to = grid[jump[0]][jump[1]]
                        if jumped_to in [0, terrain_type]: 
                            terrain_table[terrain_type] = jump
                    continue

    return grid
