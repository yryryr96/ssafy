# 인덱스를 순열로해서 sum 비교해서 최솟값 도출하면 되겠다
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
MIN = sys.maxsize
ans = 0
visited = [False]*N
def dfs(depth,idx):
    global ans,MIN
    if depth == N//2 :
        A = 0
        B = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j] :
                    A += graph[i][j]
                elif not visited[i] and not visited[j] :
                    B += graph[i][j]
        ans = abs(A-B)
        if MIN > ans :
            MIN = ans
        return

    for i in range(idx,N):
        if not visited[i] :
            visited[i] = True
            dfs(depth+1,i+1)
            visited[i] = False
dfs(0,0)
print(MIN)
