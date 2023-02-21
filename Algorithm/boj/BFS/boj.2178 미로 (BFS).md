# boj.2178 미로 (BFS)

```python
from collections import deque

N,M = map(int,input().split())
graph = [list(map(int,input())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
point = [[0,1],[1,0],[0,-1],[-1,0]]

def bfs(i,j):

    q = deque()
    q.append((i,j))
    visited[i][j] = 1 # 방문처리와 동시에 시작점도 센다고 했으므로 1로 설정
    while q:
        now = q.popleft()
        if now == (N-1,M-1) :# 시작점을 (0,0)으로 생각하고 풀었기 때문에 도착지점도 -1씩 해서 생각
            return visited[N-1][M-1]

        for di,dj in point :
            ni,nj = now[0]+di, now[1]+dj
            if 0<= ni < N and 0<= nj < M and visited[ni][nj] == 0 and graph[ni][nj] == 1:
            # 델타 이동한 좌표가 범위 내에 있고 방문한적이 없으며 이동한 좌표의 값이 1이면
                q.append((ni,nj))
                visited[ni][nj] = visited[now[0]][now[1]] + 1
                # 방문처리와 동시에 몇번 이동했는지 저장
    return 0

print(bfs(0,0))
```

bfs를 통해 최단거리 탐색하는 문제