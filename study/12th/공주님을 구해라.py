# 방법 2
# 3차원 방문 배열 안쓰고 2 만났을때 그 위치 visited랑 n-1,m-1 까지의 거리 ( 맨해튼 거리 ) 더해준 값을 따로 정해놓고
# bfs 다 돌았을 때 visited[n-1][m-1] 이랑 비교해서 더 작은 값이 답
import sys
from collections import deque
input = sys.stdin.readline

n,m,t = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[[-1]*m for _ in range(n)] for _ in range(2)]
point = [[0,1],[1,0],[0,-1],[-1,0]]

def bfs():
    q = deque()
    q.append((0,0,0)) # 좌표, 그람 상태
    if graph[0][0] == 2 :
        q.append((0,0,1))
        visited[1][0][0] = 0
    else :
        q.append((0,0,0))
        visited[0][0][0] = 0

    while q :
        i,j,gram = q.popleft()

        for di,dj in point :
            ni,nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < m :
                if gram == 0 :
                     if visited[0][ni][nj] == -1 :
                        if graph[ni][nj] == 0 :
                            visited[0][ni][nj] = visited[0][i][j] + 1
                            q.append((ni,nj,0))
                        elif graph[ni][nj] == 2 :
                            visited[1][ni][nj] = visited[0][i][j] + 1
                            q.append((ni,nj,1))
                else :
                    if visited[1][ni][nj] == -1 :
                        visited[1][ni][nj] = visited[1][i][j] + 1
                        q.append((ni,nj,1))
    return

bfs()
a = 1e9
b = 1e9
if visited[0][n-1][m-1] != -1 and visited[0][n-1][m-1] <= t :
    a = visited[0][n-1][m-1]
if visited[1][n-1][m-1] != -1 and visited[1][n-1][m-1] <= t :
    b = visited[1][n-1][m-1]

ans = min(a,b)
if ans == -1 or ans > t :
    print('Fail')
else :
    print(ans)
