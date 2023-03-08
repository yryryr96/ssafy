from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
ans = 0
board = [0]*N

def promising(row):
    for i in range(row):
        if board[row] == board[i] or abs(board[row] - board[i]) == abs(row-i) :
            return False
    return True

def dfs(row):
    global ans

    if row == N:
        ans += 1
    else:
        for i in range(N):
            board[row] = i
            if promising(row):
                dfs(row+1)
dfs(0)
print(ans)
