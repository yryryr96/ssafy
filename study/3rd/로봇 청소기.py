N, M = map(int,input().split())
r,c,dir = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
point = [[-1,0],[0,1],[1,0],[0,-1]] # 북,동,남,서

def move():
    global cnt,r,c,dir

    while True:
        if graph[r][c] == 0:
            graph[r][c] = 2 # 청소 완료한 구역을 2로 표시

        else :
            pass
        cnt = 0
        for di,dj in point :
            ni,nj = r+di, c+dj
            if 0<=ni<N and 0<=nj<M and graph[ni][nj] == 0 : # 4방향 빈칸 세기
                cnt += 1

        if cnt == 0:    # 빈칸이 없다면
            ki,kj = r + point[(dir+2)%4][0], c + point[(dir+2)%4][1]    # 후진하지만 보고있는 방향은 그대로
            if 0<=ki<N and 0<=kj<M and graph[ki][kj] != 1 :             # 후진하는 칸이 범위안에 있고 벽이 아닐때
                r,c = ki,kj
            else:   # 범위에 벗어나거나 벽이면 멈춤
                return

        else:
            dir = (dir+3)%4 # 방향 자체가 반시계 회전
            ki,kj = r + point[dir][0], c + point[dir][1]
            if 0<=ki<N and 0<=kj<M and graph[ki][kj] == 0 : # 회전해서 한칸앞이 빈칸이라면
                r,c = ki,kj

move()
ans = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            ans += 1
print(ans)
