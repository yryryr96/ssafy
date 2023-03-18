# bfs
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)
graph = [input().rstrip() for _ in range(m)]
visited = [[-1] * n for _ in range(m)]
point = [[0, 1], [1, 0], [0, -1], [-1, 0]]

q = deque()
q.append((0, 0))
visited[0][0] = 0

while q:
    now = q.popleft()

    if now == (m - 1, n - 1):
        print(visited[now[0]][now[1]])
        break

    for di, dj in point:
        ni, nj = now[0] + di, now[1] + dj
        if 0 <= ni < m and 0 <= nj < n and visited[ni][nj] == -1:

            if graph[ni][nj] == '0':
                visited[ni][nj] = visited[now[0]][now[1]]
                q.appendleft((ni, nj))
            elif graph[ni][nj] == '1':
                visited[ni][nj] = visited[now[0]][now[1]] + 1
                q.append((ni, nj))

        # 거리가 중요한게 아니고 벽 몇개 부수는지가 중요하니 '0'일때 appendleft, '1'일때 append
        # > 우선순위 부여
