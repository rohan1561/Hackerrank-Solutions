def nextMove(n,r,c,grid):
    y_pos = 0
    for g in grid:
        if 'p' in g:
            x_pos = g.index('p')
            break
        y_pos += 1
    if x_pos < c:
        return 'LEFT'
    elif x_pos > c:
        return 'RIGHT'
    elif y_pos <  r:
        return 'UP'
    elif y_pos > r:
        return 'DOWN'
    
    print(x_pos, y_pos)


n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
