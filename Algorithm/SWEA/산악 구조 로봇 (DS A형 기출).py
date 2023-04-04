from collections import deque

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    INF = int(1e9)
    visited = [[INF]*n for _ in range(n)]
    point = [[0,1],[1,0],[0,-1],[-1,0]]
    visited[0][0] = 0

    q = deque()
    q.append((0,0))
    while q :
        now = q.popleft()
        for di,dj in point :
            ni,nj = now[0] + di, now[1] + dj
            if 0<=ni<n and 0<=nj<n :
                charge = 0
                if graph[ni][nj] > graph[now[0]][now[1]]  :
                    charge = (graph[ni][nj] - graph[now[0]][now[1]])*2
                elif graph[ni][nj] == graph[now[0]][now[1]] :
                    charge = 1
                else :
                    charge = 0

                if visited[ni][nj] > visited[now[0]][now[1]] + charge :
                    visited[ni][nj] = visited[now[0]][now[1]] + charge
                    q.append((ni,nj))

    ans = visited[n-1][n-1]
    print(f'#{tc} {ans}')


