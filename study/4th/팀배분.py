import sys
input = sys.stdin.readline

# 싫어하는 사람 인접리스트 만들어서 dfs 돌며 1,-1 번갈아 visited에 대입
# 인접 리스트에 포함돼있는 사람들은 서로 싫어하는 사람들이니까 합쳐지면 안된다.
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

def dfs(v,t):
    visited[v] = t
    for i in range(1,n+1):
        if i in graph[v] and visited[i] == 0:
            dfs(i,-t)


for i in range(1,n+1):
    if visited[i] == 0 :
        dfs(i,1)

print(visited.count(1))
for i in range(1,n+1):
    if visited[i] == 1:
        print(i,end=' ')
print()
print(visited.count(-1))
for i in range(1,n+1):
    if visited[i] == -1 :
        print(i,end=' ')