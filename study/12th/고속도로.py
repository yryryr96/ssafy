import sys
import heapq

INF = sys.maxsize // 2
n, m, s, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
pq = []
max_cost = 0
min_time = 0
for _ in range(m):
    p, r, c, t = map(int, sys.stdin.readline().split())
    graph[p].append((r, t, c))
    graph[r].append((p, t, c))
    max_cost = max(max_cost, n*c)   # 최대 비용
    min_time = max(min_time, n*t)   # 최대 시간
# 최대 노드 100개 , 비용, 시간 최대 100 이므로 최대 비용 = 최대 시간 = 10000 으로 설정하고 해도 상관 없다.
times = [[INF] * (n+1) for _ in range(max_cost+1)]
# times[i][j] : i 비용으로 j 노드까지 times[i][j] 시간이 걸린다
def dijk():
    times[0][s] = 0
    heapq.heappush(pq, (0, 0, s))
    while pq:
        cur_time, cur_cost, cur = heapq.heappop(pq)
        if cur_time <= times[cur_cost][cur]:
            # print(cur_time, cur_cost, cur)
            for nxt, time, cost in graph[cur]:
                nxt_cost = cur_cost + cost  # 다음 노드까지의 비용
                nxt_dist = cur_time + time  # 다음 노드까지의 시간

                if nxt_cost <= max_cost and nxt_dist < times[nxt_cost][nxt]:
                    times[nxt_cost][nxt] = nxt_dist
                    # print(cur,nxt,cur_cost,nxt_cost)
                    heapq.heappush(pq, (nxt_dist, nxt_cost, nxt))

dijk()
# print(graph)
ans = 0
for i in range(max_cost + 1):
    if times[i][e] != INF and times[i][e] < min_time:
        ans += 1
        # print(f'#{i}',times[i][e],min_dist)
        # print(i,e)
        min_time = times[i][e]

print(ans)

# 비용이 커지면 시간은 줄어야한다.