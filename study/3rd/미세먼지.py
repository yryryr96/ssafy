import sys
input = sys.stdin.readline
N,M,T = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

def div():
    point = [[1,0],[0,1],[-1,0],[0,-1]]
    temp_list =[[0]*(M) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and graph[i][j] != -1 :
                temp = 0
                for di,dj in point :
                    ni,nj = i+di, j+dj
                    if 0<=ni<N and 0<=nj<M and graph[ni][nj] != -1 :
                        temp_list[ni][nj] += graph[i][j]//5
                        temp += graph[i][j]//5
                graph[i][j] -= temp
    for i in range(N):
        for j in range(M):
            graph[i][j] += temp_list[i][j]

div()
for i in range(N):
    print(*graph[i])