from collections import deque
import sys
input = sys.stdin.readline

M,N,H = map(int,input().split())
graph = []
q = deque()

for i in range(H):  # 층
    temp = []
    for j in range(N):  # 평면에서 세로
        temp.append(list(map(int,input().split())))
        for k in range(M):  # 평면에서 가로
            if temp[j][k] == 1:
                q.append((k,j,i)) # q에는 x,y,z 순으로 저장
    graph.append(temp) # i층에 평면 저장

dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

while q:
    x,y,z = q.popleft()

    for i in range(6):
        nx = x+dx[i]
        ny = y+dy[i]
        nz = z+dz[i]
        if 0 <= nx < M and 0<=ny < N and 0<=nz<H and graph[nz][ny][nx] == 0 :
            # graph[nz][ny][nz] : graph의 nz층에 있는 평면에서 ny,nz 값
            q.append((nx,ny,nz))
            graph[nz][ny][nx] = graph[z][y][x] + 1

ans = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0 :
                print(-1)
                exit()
            else :
                if ans < graph[i][j][k] : 
                    # 좌표값에 이미 거리값이 저장돼 있으므로 맥스값 갱신
                    ans = graph[i][j][k]
print(ans-1) # 처음에 1로 설정해뒀기 때문에 -1 해줌