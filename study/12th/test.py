import heapq,sys
input = sys.stdin.readline

n, m, s, e = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, c, t = map(int, input().split())
    graph[u-1].append((v-1, c, t))
    graph[v-1].append((u-1, c, t))

def dijkstra(start):
    dist = [[float('inf'), float('inf')] for _ in range(n)]
    dist[start] = [0, 0]  # 초기값 설정
    pq = []
    heapq.heappush(pq, (0, 0, start))  # (비용, 시간, 노드) 순으로 저장
    while pq:
        cur_cost, cur_time, cur_node = heapq.heappop(pq)
        if dist[cur_node][0] < cur_cost or (dist[cur_node][0] == cur_cost and dist[cur_node][1] < cur_time):
            continue  # 이미 노드의 최단 경로를 찾았을 경우 스킵
        for nxt_node, cost, time in graph[cur_node]:
            new_cost, new_time = cur_cost+cost, cur_time+time
            if dist[nxt_node][0] > new_cost or (dist[nxt_node][0] == new_cost and dist[nxt_node][1] > new_time):
                dist[nxt_node] = [new_cost, new_time]
                heapq.heappush(pq, (new_cost, new_time, nxt_node))
    return dist

result = dijkstra(s-1)
count = 0
for i in range(n):
    if result[i][0] == result[e-1][0] and result[i][1] == result[e-1][1]:
        count += 1

print(count)
