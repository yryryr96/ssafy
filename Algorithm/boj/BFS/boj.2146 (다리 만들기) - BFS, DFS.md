# boj.2146 (다리 만들기)

```python
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10001)

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
island = -1

point = [[0,1],[1,0],[0,-1],[-1,0]]

def dfs(i,j,island):		# 섬을 구분려고 dfs로 섬마다 다른 숫자로 바꾸기위해 사용
    graph[i][j] = island
    visited[i][j] = 1
    for di,dj in point:
        ni,nj = i+di,j+dj
        if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 :
            if graph[ni][nj] == 1 :
                dfs(ni,nj,island)

for i in range(N):			# dfs 적용해서 섬 구분
    for j in range(N):
        if graph[i][j] == 1 :
            dfs(i,j,island)
            island -= 1

MIN = 10000

def bfs(i,j) :
    global MIN
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    while q :
        now = q.popleft()
        for di,dj in point :
            ni,nj =  now[0]+di, now[1] + dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 : # 좌표가 범위를 벗어나지 않고 방문한적이 없으면
                if graph[ni][nj] == 0 :	# 바다일 때 칸을 진행하기위해 q에 push
                    q.append((ni,nj))
                    visited[ni][nj] = visited[now[0]][now[1]] + 1 # 방문처리를 하는것과 동시에 거리 표현
                elif graph[ni][nj] != graph[i][j] :		# 바다일 때는 위에서 걸러주니 다른 섬을 만날 때
                    if visited[now[0]][now[1]] < MIN:	# MIN 값 갱신하고 함수 종료
                        MIN = visited[now[0]][now[1]]
                    return MIN

lst = deque()		# 바다와 붙어있는 좌표들만 조사하기 위해 해당 좌표들만 미리 리스트에 저장
for i in range(N):	
    for j in range(N):
        if graph[i][j] != 0 :
            for di,dj in point:
                ni,nj = i+di,j+dj
                if 0<=ni<N and 0<=nj<N and graph[ni][nj] == 0:
                    lst.append((i,j))
                    break
for i,j in lst :
    bfs(i,j)
    visited = [[0 for _ in range(N)] for _ in range(N)]

ans = MIN - 1	# bfs 실행 시 visited 값이 1로 시작하므로 MIN값에서 1 빼준 값이 거리
print(ans)
```