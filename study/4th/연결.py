import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(m + 1)]
visited = [[0] * (n + 1) for _ in range(m + 1)]
point = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for _ in range(2):
    x, y = map(int, input().split())
    graph[y][x] = 1

for _ in range(2):
    x, y = map(int, input().split())
    graph[y][x] = 2

for i in range(m + 1):
    print(*graph[i])


def bfs(i, j):
    q = deque
    q.append((i, j))
    visited[i][j] = 1

    while q:
        now = q.popleft()
        if graph[now[0]][now[1]] == graph[i][j]:
            return

        for di, dj in point:
            ni, nj = now[0] + di, now[1] + dj
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
                if graph[ni][nj] == 0:
                    visited[ni][nj] = visited[now[0]][now[1]] + 1



