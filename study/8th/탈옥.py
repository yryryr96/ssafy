import sys
from collections import deque
input = sys.stdin.readline

def bfs(i,j) :
    visited = [[-1]*(m+2) for _ in range(n+2)]
    q = deque()
    q.append((i,j))
    visited[i][j] = 0
    while q:
        now = q.popleft()
        for di,dj in point :
            ni,nj = now[0] + di, now[1] + dj
            if 0<=ni<n+2 and 0<=nj<m+2 and visited[ni][nj] == -1 :
                if graph[ni][nj] == '.' or graph[ni][nj] == '$':    # 문을 안열고 지나갈 수 있는 경우
                    visited[ni][nj] = visited[now[0]][now[1]]
                    q.appendleft((ni,nj))

                elif graph[ni][nj] == '#' : # 문 열어야 되는 경우
                    visited[ni][nj] = visited[now[0]][now[1]] + 1
                    q.append((ni,nj))

    return visited

T = int(input())
for tc in range(T):
    n,m = map(int,input().split())
    graph = [['.']*(m+2)] + [['.'] + list(input().rstrip()) + ['.'] for _ in range(n)] + [['.']*(m+2)]
    point = [[0,1],[1,0],[-1,0],[0,-1]]
    criminal = []   # 범죄자 위치 좌표
    for i in range(n+2):
        for j in range(m+2):
            if graph[i][j] == '$' :
                criminal.append((i,j))

    # 범죄자와 범죄좌 독립적으로 탈출, 범죄자가 중간에 만나서 같이 탈출하는 경우를 따져주기위해 visited 따로 설정
    v1 = bfs(criminal[0][0],criminal[0][1])
    v2 = bfs(criminal[1][0],criminal[1][1])
    v3 = bfs(0,0) # 입구에서 범죄자 있는 곳으로

    MIN = sys.maxsize
    for i in range(1,n+1):
        for j in range(1,m+1):
            if v1[i][j] != -1 and v2[i][j] != -1 and v3[i][j] != -1 :
                temp = v1[i][j] + v2[i][j] + v3[i][j]
                if graph[i][j] == '#' : # 만약 3가지 경우가 모두 '#' 일때 비교한다면 문은 1개지만 1+1+1 이 되므로 -2 해준다.
                    temp -= 2
                MIN = min(temp,MIN)
    print(MIN)
    # 각각 일어날 수 있는 경우의 수를 visited로 구별해서 판별하는 방법이 신기하다