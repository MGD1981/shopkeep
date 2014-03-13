from random import randint

def get_new_world(size=128):
    world = {
        'grid': [[0] * size] * size,
        'size': size
    }
    world['grid'] = generate_terrain(world['grid'], size)
    
    return world
    
    
    
#Key: g = grassland, w = woodland, r = rockland
def generate_terrain(grid, size):
    tiles_remaining = 0
    for row in grid:
        tiles_remaining += len(row)

    g = None
    w = None
    r = None
    while g == w or w == r or r == g:
        g = (randint(0, size-1), randint(0, size-1))
        w = (randint(0, size-1), randint(0, size-1))
        r = (randint(0, size-1), randint(0, size-1))
    grid[g[0]][g[1]] = 'g'
    grid[w[0]][w[1]] = 'w'
    grid[r[0]][r[1]] = 'r'
    tiles_remaining -= 3
    while tiles_remaining > 0:
        pass
        #TODO