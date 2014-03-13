from random import randint
import pdb

def get_new_world(size=128):
    world = {
        'grid': [[0] * size] * size,
        'size': size
    }
    world['grid'] = generate_terrain(world['grid'], size)
    
    return world
    
    
    
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
   pdb.set_trace()
     tiles_remaining -= 3
    while tiles_remaining > 0:
        print "tiles_remaining: %r" % tiles_remaining

        for t in ['g', 'w', 'r']:
            print "Tile: %r" % t
            raw_input()
            for next_t in [(eval(t)[0] - 1, eval(t)[1]),
                           (eval(t)[0] + 1, eval(t)[1]),
                           (eval(t)[0], eval(t)[1] - 1),
                           (eval(t)[0], eval(t)[1] + 1)]:
                print next_t

                try:
                    if grid[next_t[0]][next_t[1]] == 0:
                        grid[next_t[0]][next_t[1]] = t
                        exec(t + " = next_t")
                        tiles_remaining -= 1
                        print "%r = %r then break" % (t, next_t)
                   
                        next                        
                except IndexError:
                    print "Index Error, continue"
                    
                    continue