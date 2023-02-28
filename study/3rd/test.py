from collections import deque
N,M,T = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
q = deque()
visited = [[0]*(M+1) for _ in range(N+1)]

for i in range(N):
    print(*graph[i])

for i in range(N):
    for j in range(M):
        if graph[i][j] != 0 and graph[i][j] != -1 :
            q.append((i,j))
            visited[i][j] = 1

point = [[0,1],[1,0],[-1,0],[0,-1]]
while q:
    now = q.popleft()
    cnt = 0
    if visited[now[0]][now[1]] == T+1:
        break
    for di,dj in point :
        ni,nj = now[0]+di, now[1]+dj
        if 0<=ni<N and 0<=nj<M :
            if graph[ni][nj] != -1 :
                graph[ni][nj] += graph[now[0]][now[1]]//5
                visited[ni][nj] = visited[now[0]][now[1]] + 1
                cnt += 1
                if graph[ni][nj] != 0 :
                    q.append((ni,nj))
    graph[now[0]][now[1]] = graph[now[0]][now[1]] - (graph[now[0]][now[1]]//5 * cnt)

for i in range(N):
    print(*graph[i])