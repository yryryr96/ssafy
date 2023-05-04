import sys,heapq
input = sys.stdin.readline

n,m,s,e = map(int,input().split())
graph = [[] for _ in range(n+1)]
INF = 1e9
for _ in range(m) :
    p,r,c,t = map(int,input().split())
    graph[p].append((r,c,t))
    graph[r].append((p,c,t))
# print(graph)
cost = [INF]*(n+1)
time = [INF]*(n+1)
def dijkstra_cost(start):
    q = []
    heapq.heappush(q,(0,start))
    cost[start] = 0
    while q :
        dist, now = heapq.heappop(q)
        if cost[now] < dist :
            continue
        for after in graph[now] :
            c = cost[now] + after[1]
            if c < cost[after[0]] :
                cost[after[0]] = c
                heapq.heappush(q,(c,after[0]))

def dijkstra_time(start):
    q = []
    heapq.heappush(q,(0,start))
    time[start] = 0
    while q :
        dist, now = heapq.heappop(q)
        if time[now] < dist :
            continue
        for after in graph[now] :
            c = time[now] + after[2]
            if c < time[after[0]] :
                time[after[0]] = c
                heapq.heappush(q,(c,after[0]))

dijkstra_cost(s)
check_c = cost[e]
dijkstra_time(s)
check_t = time[e]
min_t = sys.maxsize
min_c = sys.maxsize
visited = [0]*(n+1)
def dfs_c(v,C,T) : # time 구하기
    global check_c,check_t,min_t
    if C > check_c :
        return

    if v == e :
        min_t = min(min_t,T)
        return

    for i in graph[v] :
        if not visited[i[0]] :
            visited[i[0]] = 1
            dfs_c(i[0],C+i[1],T+i[2])
            visited[i[0]] = 0

def dfs_t(v,C,T) : # time 구하기
    global check_c,check_t,min_c
    if T > check_t :
        return

    if v == e :
        min_c = min(min_c,C)
        return

    for i in graph[v] :
        if not visited[i[0]] :
            visited[i[0]] = 1
            dfs_t(i[0],C+i[1],T+i[2])
            visited[i[0]] = 0
dfs_c(s,0,0)
dfs_t(s,0,0)
ans = 0
if check_c == min_c and check_t == min_t :
    print(1)
else :
    print(2)