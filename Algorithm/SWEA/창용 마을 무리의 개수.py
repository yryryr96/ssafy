from collections import deque

T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    graph = [[]for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    def bfs(v,cnt):
        q = deque()
        q.append(v)

        while q :
            now = q.popleft()
            for i in graph[now] :
                if not visited[i] :
                    visited[i] = cnt
                    q.append(i)

    k = 1
    visited = [0] * (n + 1)
    for i in range(1,n+1):
        if not visited[i] :
            visited[i] = k
            bfs(i,k)
            k+=1

    ans = max(visited)
    print(f'#{tc} {ans}')

