import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q :
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
    n,e = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    INF = int(1e9)
    distance = [INF]*(n+1)
    for _ in range(e):
        s,e,w = map(int,input().split())
        graph[s].append((e,w))

    dijkstra(0)
    ans = distance[n]
    print(f'#{tc} {ans}')






