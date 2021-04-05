import math
def solution(n):
    answer = [[0]*i for i in range(1,n+1)]
    count = 1
    

    for i in range(math.ceil(n/3)):
        x, y = 2*i, i
        
        while(True):
            if x < n and answer[x][y] == 0:
                answer[x][y] = count
                count += 1
                x += 1
            else:
                x -= 1
                y += 1
                break

        while(True):
            if y < n and answer[x][y] == 0:
                answer[x][y] = count
                count += 1
                y += 1
            else:
                y -= 2
                x -= 1
                break                

        while(True):
            if answer[x][y] == 0:
                answer[x][y] = count
                count += 1
                y -= 1
                x -= 1
            else:
                break 
    tmp = []
    for t in answer:
        tmp += t
    return tmp

##
from itertools import chain
def solution(n):
    [row, col, cnt] = [-1, 0, 1]
    board = [[None] * i for i in range(1, n+1)]
    for i in range(n):
        for _ in range(n-i):
            if i % 3 == 0:
                row += 1
            elif i % 3 == 1:
                col += 1
            else:
                row -= 1
                col -= 1
            board[row][col] = cnt
            cnt += 1
    return list(chain(*board))