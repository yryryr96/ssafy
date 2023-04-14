import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
# 반시계
point = [[-1,0],[0,-1],[1,0],[0,1]]
visited = [[0]*n for _ in range(n)]
MAX = 0

def dfs(i,j,day,dir):
    global ans
    if day == m :
        return ans
    temp = 0
    dir = dir+3
    for l in range(4):
        d = (dir+l)%4
        di,dj = point[d]
        ni,nj = i+di, j+dj

        if 0<=ni<n and 0<=nj<n and graph[ni][nj] == 0 : # 다음 농지가 빈칸
            if visited[ni][nj] == 0 :
                temp = 1
                break;
            elif visited[ni][nj]!= 0 and visited[ni][nj] + 3 < day : #다음 농지가 곡물
                temp = 1
                break;

    if temp == 0 :
        return ans

    else:
        if visited[i][j] == 0 : # 현재칸이 빈칸
            visited[i][j] = day
            dfs(ni,nj,day+1,d)
        else :                  # 현재칸이 곡물
            visited[i][j] = 0
            ans += 1
            dfs(ni,nj,day+1,d)
    return ans

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0 :
            for k in range(4):
                ans = 0
                visited = [[0] * n for _ in range(n)]
                check = dfs(i,j,1,k)
                if check > MAX :
                    MAX = check

print(MAX)