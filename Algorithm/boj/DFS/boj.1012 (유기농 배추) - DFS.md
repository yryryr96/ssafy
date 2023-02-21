# boj.1012 (유기농 배추) - DFS

```python
from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(i,j):
	point = [[0,1],[1,0],[-1,0],[0,-1]]
    graph[i][j] = 0
    visited[i][j] = 1

    for di,dj in point:
        ni,nj = i+di,j+dj
        if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0 and graph[ni][nj] == 1:
        # 그래프의 범위 내에 있으며 방문한적이 없고 이동한 그래프의 값이 1일 때
            dfs(ni,nj)

T = int(input())
for tc in range(T):
    M, N, K = map(int,input().split()) # 가로, 세로, 배추 수
    graph = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    bug = 0

    for n in range(K):
        b,a = map(int,input().split()) # 열,행 입력
        graph[a][b] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 :
                dfs(i,j)
                bug += 1

    print(bug)
```

