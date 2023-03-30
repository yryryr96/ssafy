from collections import deque
T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    lst = list(map(int,input().split()))
    visited = [0]*(n+1)
    for i in range(0,len(lst),2):
        graph[lst[i]].append(lst[i+1])
        graph[lst[i+1]].append(lst[i])

    def bfs(v):
        q = deque()
        q.append(v)
        visited[v] = 1
        while q:
            now = q.popleft()
            for i in graph[now] :
                if visited[i] == 0 :
                    visited[i] = 1
                    q.append(i)
    ans = 0
    for i in range(1,n+1):
        if visited[i] == 0 :
            ans += 1
            bfs(i)

    print(f'#{tc} {ans}')


