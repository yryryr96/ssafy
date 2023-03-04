# 0일때 마다 bfs -> 시간이 느리다. -> SWEA 물놀이 문제랑 똑같다 -> 1일때 동시에 돌려서 최대거리 계산
import sys
from collections import deque
input = sys.stdin.readline

def bfs(i,j):
    point = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((i,j))
    visited[i][j] = 1

    while q:
        now = q.popleft()
        for di,dj in point :
            ni,nj = now[0] + di, now[1] + dj
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0 :
                visited[ni][nj] = visited[now[0]][now[1]] + 1
                q.append((ni,nj))
                if graph[ni][nj] == 1 :
                    ANS.append(visited[ni][nj] - 1)
                    return

N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
ANS = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 :
            bfs(i,j)

print(max(ANS))