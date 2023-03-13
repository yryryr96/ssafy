import sys
import heapq
input = sys.stdin.readline

<<<<<<< HEAD
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
=======
n,m = map(int,input().split())
start = 1
INF = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist :
            continue
        for after in graph[node] :
            cost = distance[node] + after[1]
            if cost < distance[after[0]] :
                distance[after[0]] = cost
                heapq.heappush(q,(cost,after[0]))

dijkstra(start)
print(distance[n])

>>>>>>> 953ecda4651fa7b516bc3f1e411661519f4eda6d
