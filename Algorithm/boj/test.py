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
white = []
white_check = []
blue = []
blue_check = []
def dfs(v,lst,lst1):
    global visited
    visited[v] = 1
    lst1.append(v)
    for a in graph[v] :
        if a not in lst:
            lst.append(a)

    for i in range(1,n+1):
        if i not in white_check and visited[i] == 0 :
            dfs(i,white_check,white)
        if i not in blue_check and visited[i] == 0 :
            dfs(i,blue_check,blue)

        if len(blue) + len(white) == n :
            print(white_check,blue_check)
            print(len(white))
            print(*white)
            print(len(blue))
            print(*blue)
            print('#')
            return
        else:

            continue

dfs(1,white_check,white)

