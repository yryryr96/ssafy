import sys
input = sys.stdin.readline

n,k = map(int,input().split())
graph = [[0]*(k+1) for _ in range(n+1)]
lst = [(0,0)]
for _ in range(n):
    w,v = map(int,input().split())
    lst.append((w,v))

for i in range(1,n+1):
    for j in range(1,k+1):
        weight = lst[i][0]
        value = lst[i][1]

        if j < weight :
            graph[i][j] = graph[i-1][j]
        else :
            graph[i][j] = max(graph[i-1][j], graph[i-1][j-weight]+value)

print(graph[n][k])