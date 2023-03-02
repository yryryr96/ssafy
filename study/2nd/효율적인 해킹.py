import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    B,A = map(int,input().split())  # 방향성 A에서 B로 향한다.
    graph[A].append(B)

def bfs(v): # 단방향으로 연결되어 있는 곳 탐색
    cnt = 1
    q = deque([v])
    visited = [0] * (N + 1)
    visited[v] = 1

    while q :
        now = q.popleft()
        for i in graph[now] :
            if visited[i] == 0 :
                visited[i] = 1
                cnt += 1
                q.append(i)
    return cnt
MAX = 0
ans = []
for i in range(1,N+1):
    cnt = bfs(i)
    if cnt > MAX :
        MAX = cnt
        ans.clear()
        ans.append(i)

    elif cnt == MAX :
        ans.append(i)

print(*ans)
# Pypy 로 제출해서 겨우 통과..