# 다익스트라 2번 써줘서 x에서 각 집까지 최소 거리, 각 집에서 x까지의 최소거리 더해서 최대값 도출
import heapq
def dijkstra(start,distance):
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

T = int(input())
for tc in range(1,T+1):
    n,m,x = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m): # a에서 b로 갈때 c시간
        a,b,c, = map(int,input().split())
        graph[a].append((b,c))

    INF = int(1e9)
    MAX = 0

    distancex = [INF]*(n+1)
    dijkstra(x,distancex)

    for i in range(1,n+1):
        distance = [INF] * (n + 1)
        if i != x :
            dijkstra(i,distance)
            MAX = max(MAX,distance[x]+distancex[i])

    print(f'#{tc} {MAX}')
