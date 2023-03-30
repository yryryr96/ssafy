def dfs(idx,depth):
    global MIN
    if depth == n//2 :
        A,B = 0,0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j] :
                    A += graph[i][j]
                elif not visited[i] and not visited[j] :
                    B += graph[i][j]

        MIN = min(MIN,abs(A-B))
        return

    for i in range(idx,n):
        if visited[i] == 0 :
            visited[i] = 1
            dfs(i+1,depth+1)
            visited[i] = 0
    return

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    visited = [0]*n
    MIN = 1e9
    dfs(0,0)
    print(f'#{tc} {MIN}')


