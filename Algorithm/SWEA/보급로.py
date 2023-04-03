from collections import deque

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    graph = [list(map(str,input())) for _ in range(n)]
    point = [[0,1],[1,0],[-1,0],[0,-1]]
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        graph[i] = list(map(int,graph[i]))

    INF = int(1e9)
    distance = [[INF]*n for _ in range(n)]
    q = deque()
    q.append((0,0))
    distance[0][0] = 0

    while q :
        now = q.popleft()
        for di,dj in point :
            ni,nj = now[0] + di, now[1] + dj
            if 0<=ni<n and 0<= nj <n :
                if distance[ni][nj] > distance[now[0]][now[1]] + graph[ni][nj] :
                    distance[ni][nj] = distance[now[0]][now[1]] + graph[ni][nj]
                    q.append((ni,nj))

    print(f'#{tc} {distance[n-1][n-1]}')

