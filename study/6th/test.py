import sys
input = sys.stdin.readline

point = [[0,1],[1,0],[-1,0],[0,-1]]

n,m,h = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            s,e = i,j
            break
MAX = 0
def dfs(i,j,hp,cnt):
    global MAX

    if hp == 0 :
        return

    for di,dj in point:
        ni,nj = i+di,j+dj
        if 0<=ni<n and 0<=nj<n :
            if graph[ni][nj] == 2:
                graph[ni][nj] = 0
                dfs(ni,nj,hp+h-1,cnt+1)

            elif graph[ni][nj] == 1:
                if MAX < cnt+1:
                    MAX = cnt
                continue

            else:
                dfs(ni,nj,hp-1,cnt)
    return MAX

print(dfs(s,e,m,0))
