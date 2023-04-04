import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
temp = [[0]*n for _ in range(n)]
def dfs(v):

    for j in range(n):
        if graph[v][j] == 1 :
            if temp[v][j] == 0 :
                temp[v][j] = 1
                dfs(j)

for i in range(n):
    dfs(i)
print(temp)