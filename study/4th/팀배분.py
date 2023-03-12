import sys
input = sys.stdin.readline

n = int(input())
visited = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for i in range(1,n+1):
    lst = list(map(int,input().split()))
    l = lst[0]
    for j in range(1,l+1):
        if lst[j] not in graph[i] :
            graph[i].append(lst[j])
        if i not in graph[lst[j]] :
            graph[lst[j]].append(i)

print(graph)
def dfs(v):
