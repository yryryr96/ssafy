# SWEA.물놀이를 가자

```python
from collections import deque
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    graph = [list(input()) for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    q = deque()


    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'W' :
                q.append((i,j))
                visited[i][j] = 1

    def bfs():
        point = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while q :
            now = q.popleft()
            for di,dj in point:
                ni,nj = now[0] + di, now[1] + dj
                if 0<= ni < N and 0<= nj < M and visited[ni][nj] == 0 :
                    q.append((ni,nj))
                    visited[ni][nj] = visited[now[0]][now[1]] + 1

    bfs()
    ans = 0
    for i in range(N):
        for j in range(M):
           ans+=(visited[i][j] - 1)

    print(f'#{tc} {ans}')
```

맨 밑에 ans를 리스트로 받아서 append 한다음에 sum 하는거보다 저렇게 바로 더해주는게 메모리도 덜 잡아먹는것인가?