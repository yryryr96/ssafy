from collections import deque
import sys
input = sys.stdin.readline
tc = 1
while True :

    n = int(input())
    if n == 0 :
        break
    INF = int(1e9)
    visited = [[INF]*n for _ in range(n)]
    graph = [list(map(int,input().split())) for _ in range(n)]
    point = [[0,1],[1,0],[-1,0],[0,-1]]
    q = deque()
    visited[0][0] = graph[0][0]
    q.append((0,0))
    while q:
        now = q.popleft()
        for di,dj in point :
            ni,nj = now[0] + di, now[1]+dj
            if 0<=ni<n and 0<=nj<n :
                if graph[ni][nj] + visited[now[0]][now[1]] < visited[ni][nj] :
                    q.append((ni,nj))
                    visited[ni][nj] = graph[ni][nj] + visited[now[0]][now[1]]
    print(f'Problem {tc}: {visited[n - 1][n - 1]}')
    tc += 1
