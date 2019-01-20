#!/bin/python3

def closest_dirty(x, y, board):
    dirt = []
    index1 = 0
    for i in board:
        index2 = 0
        for j in i:
            if j == 'd':
                dirt.append([index1, index2])
            index2 += 1
        index1 += 1
    dirt = sorted(dirt, key = lambda t: abs(t[0]-x) + abs(t[1]-y))
    return dirt [0]


def nextMove(posr, posc, board):
    if board[posr][posc] == 'd':
        return 'CLEAN'
    c = closest_dirty(posr, posc, board)
    if c[0] > posr:
        return 'DOWN'
    elif c[0] < posr:
        return 'UP'
    elif c[1] > posc:
        return 'RIGHT'
    elif c[1] < posc:
        return 'LEFT'
    
    
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    print(nextMove(pos[0], pos[1], board))
