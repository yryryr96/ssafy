# boj.1697 (숨바꼭질) - BFS

```python
from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

graph = [[] for _ in range(100001)]
visited = [0]*100001
N,K = map(int,input().split())
def bfs(v,K):

    visited[v] = 1
    q = deque()
    q.append(v)

    while q:

        now = q.popleft()
        if now == K:
            return visited[now] - 1

        for after in [now+1,now-1,now*2] :	# 이 세가지 값에 대해서만 비교
            if 0<= after <= 100000 and visited[after] == 0 :
                q.append(after)
                visited[after] = visited[now] + 1

print(bfs(N,K))
```

```python
from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

graph = [[] for _ in range(100001)]
visited = [0]*100001
N,K = map(int,input().split())
def bfs(v,K):

    visited[v] = 1
    q = deque()
    q.append(v)

    while q:

        now = q.popleft()
        if now == K:
            return visited[now] - 1

        graph[now].append(now-1)	# 인접리스트에 직접 추가
        graph[now].append(now+1)
        graph[now].append(now*2)

        for after in graph[now] :
            if 0<= after <= 100000 and visited[after] == 0 :
                q.append(after)
                visited[after] = visited[now] + 1

print(bfs(N,K))
```

