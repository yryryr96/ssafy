import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
point = [[0,1],[1,0],[-1,0],[0,-1]]

def bfs():
    q = deque()

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                for di,dj in point :
                    ni,nj = i+di,j+dj
                    if 0<=ni<n and 0<=nj<m and graph[ni][nj] == 0 :
                        q.append((ni,nj))
                        break

    for i,j in q:
        graph[i][j] = 0
