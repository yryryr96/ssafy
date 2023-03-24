import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(p1,p2):
    visited = [-1]*(n+1)
    q = deque()
    q.append(p1)
    q.append(p2)
    visited[0] = 0
    visited[p1] = 0
    visited[p2] = 0

    while q:
        now = q.popleft()
        for i in graph[now] :
            if i != p1 and i!= p2 and visited[i] == -1 :
                visited[i] = visited[now] + 2
                q.append(i)
    ans = sum(visited)
    return ans

ANS = []
MIN = sys.maxsize
for i in range(1,n):
    for j in range(i+1,n+1):
        check = bfs(i,j)
        if MIN > check :
            MIN = check
            ANS.append((i,j,MIN))

ANS.sort(key=lambda x : (x[2],x[0],x[1]))

print(*ANS[0])


