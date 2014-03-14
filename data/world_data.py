from random import randint, choice, shuffle

def get_new_world(size=64):
    world = {
        'grid': [list([0] * size) for x in xrange(size)],
        'size': size
    }
    world['grid'] = generate_terrain(world['grid'], size)
    
    return world
    
    
# Key: g=grassland, w=woodland, r=rockland
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
        for t in ['g', 'w', 'r']:
            checked_tiles = 0
            adjacents = [(eval(t)[0] - 1, eval(t)[1]),
                         (eval(t)[0] + 1, eval(t)[1]),
                         (eval(t)[0], eval(t)[1] - 1),
                         (eval(t)[0], eval(t)[1] + 1)]
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
                            exec(t + " = " + str(jump))
                    continue    
                if grid[next_t[0]][next_t[1]] == 0:
                    grid[next_t[0]][next_t[1]] = t
                    exec(t + " = next_t")
                    tiles_remaining -= 1
                else:
                    checked_tiles += 1
                    checked_tiles += 1
                    if checked_tiles == 4:
                        jump = (randint(0, size-1), randint(0, size-1))
                        jumped_to = grid[jump[0]][jump[1]]
                        if jumped_to in [0, t]: 
                            exec(t + " = " + str(jump))
                    continue

    return grid
