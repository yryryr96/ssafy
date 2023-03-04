from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
shark = 2
point = [[0,1],[1,0],[0,-1],[-1,0]]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9 :
            graph[i][j] = 0
            now = (i,j)

ans = 0
cnt = 0
while True:
    lst = []    # 거리,좌표 저장할 리스트
    visited = [[0 for _ in range(N)] for _ in range(N)]
    q = deque()
    q.append(now)
    visited[now[0]][now[1]] = 1
    while q :
        now = q.popleft()
        for di,dj in point :
            ni,nj = now[0]+di, now[1]+dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 and graph[ni][nj] <= shark :    # 샤크값보다 작거나 같은 좌표만 탐색
                q.append((ni,nj))
                visited[ni][nj] = visited[now[0]][now[1]] + 1

                if 0 < graph[ni][nj] < shark :  # 샤크값 보다 작으면 잡아먹기위해 리스트에 저장
                    lst.append([visited[ni][nj],ni,nj])

    if not lst :    # 잡아 먹을 물고기가 없으면 멈춤
        break

    lst.sort(key=lambda x: (x[0], x[1], x[2])) # 행, 열 위치가 답에 연관돼있기 때문에 작은거부터 정렬
    graph[lst[0][1]][lst[0][2]] = 0 # 현재 잡아먹은 물고기 위치를 0으로 바꿈
    now = (lst[0][1], lst[0][2])    # 현재 위치를 잡아먹은 물고기 위치로 갱신 -> 다음 while문 돌면서 같은 작업 반복
    cnt += 1    # 샤크 값보다 작은놈 잡아먹은 횟수
    if cnt == shark :   # 그만큼 잡아먹으면 샤크 값 +1
        shark += 1
        cnt = 0 # 잡아먹은 횟수 초기화
    ans += lst[0][0] - 1 # 좌표 이동할때마다 거리 더해줌

print(ans)
