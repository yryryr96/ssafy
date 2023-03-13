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

white = []
white_check = []
blue = []
def dfs(v):
    visited[v] = 1
    white.append(v)
    for a in graph[v] :
        if a not in white_check:
            white_check.append(a)

    for i in range(1,n+1):
        if i not in white_check and visited[i] == 0 :
            dfs(i)

dfs(1)

for i in range(1,n+1):
    if i not in white:
        blue.append(i)

print(len(white))
print(*white)
print(len(blue))
print(*blue)