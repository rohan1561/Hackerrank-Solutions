#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    n = int((n-1)/2)
    if 'p' in grid[0]:
        if grid[0][0] == 'p':
            answer = n*'UP\nLEFT\n'
        else:
            answer = n*'UP\nRIGHT\n'
    if 'p' in grid[-1]:
        if grid[-1][0] == 'p':
            answer = n*'DOWN\nLEFT\n'
        else:
            answer = n*'DOWN\nRIGHT\n'
    answer = answer.strip('\n')
    return answer

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())
print(displayPathtoPrincess(m,grid))
