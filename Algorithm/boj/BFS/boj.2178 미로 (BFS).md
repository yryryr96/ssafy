# boj.2178 미로 (BFS)

```python
from collections import deque
N,M = map(int,input().split())
graph = [list(map(int,input())) for _ in range(N)]
visited = [[0 for _ in range(M+1)] for _ in range(N+1)]
point = [[0,1],[1,0],[0,-1],[-1,0]]

def bfs(i,j):

    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    while q:
        now = q.popleft()
        if now == (N-1,M-1) :
            return visited[N-1][M-1]

        for di,dj in point :
            ni,nj = now[0]+di, now[1]+dj
            if 0<= ni < N and 0<= nj < M and visited[ni][nj] == 0 and graph[ni][nj] == 1:
                q.append((ni,nj))
                visited[ni][nj] = visited[now[0]][now[1]] + 1

print(bfs(0,0))
```

bfs를 통해 최단거리 탐색하는 문제