# Dijkstra (데이크스트라)

<img src="https://blog.kakaocdn.net/dn/bysx8O/btrftofXLDl/vJLp0dOk2U8A1YE9SuQ9x1/img.png" alt="img" style="zoom: 33%;" />

<img src="https://blog.kakaocdn.net/dn/c7jlZz/btrfFEVRizL/OIDKfob2QMrMnVcOb6nBTk/img.png" alt="img" style="zoom: 33%;" />

<img src="https://blog.kakaocdn.net/dn/cTeEYD/btrfzjZfwyq/cYKGlq1kjNMamdW6pDRz1k/img.png" alt="img" style="zoom:33%;" />

```python
INF = int(1e9)

n,m = map(int,input().split())  # 노드의 개수, 간선의 개수
start = int(input())    # 시작 노드
graph = [[] for _ in range(n+1)]    # 인접리스트
visited = [0] * (n+1)   # 방문 테이블
distance = [INF] * (n+1) # 거리 테이블

for _ in range(m):
    a,b,c = map(int,input().split()) # 시작노드, 인접노드, 가중치
    graph[a].append((b,c))

def get_smallest_node(): # 방문하지 않았고 거리값이 가장 작은 인덱스(노드번호) 리턴
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start): # 단방향이고 모든 가중치가 0 이상일때만 사용 가능
    distance[start] = 0
    visited[start] = 1

    for i in graph[start]:
        distance[i[0]] = i[1] # i[0] : 연결 노드, i[1] : 가중치

    for _ in range(n-1):
        now = get_smallest_node()   # 시작노드에서 거리가 가장 짧은 노드
        visited[now] = 1

        for after in graph[now] :
            cost = distance[now] + after[1]
            if cost < distance[after[0]] :
                distance[after[0]] = cost

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print('도달 불가')
    else :
        print(distance[i])
```

##### 다익스트라 알고리즘은 그래프에서 여러 개의 노드가 존재할 때, 특정한 노드에서 출발해 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘이다. 그래프의 방향성이 존재하고 간선의 가중치가 0 이상의 양수일 때 정상적으로 동작한다.

1. 출발 노드를 설정
2. 최단 거리 테이블을 초기화 (최단거리 테이블 정의) (distance)
3. 방문 테이블 정의 (visited)
4. 해당 노드를 거쳐 다른 노드로 가는 가중치를 계산해 최단거리 테이블 업데이트
5. 3,4 반복

방문처리한 노드의 인접노드의 거리값은 갱신되어야한다. 또한, 방문하지 않은 노드 중 갱신한 테이블 기준으로 시작노드와 가장 최단거리인 노드를 탐색해야한다. 거리비용이 동일할 때는 노드 번호가 작은것부터 탐색

**다익스트라 알고리즘은 방문하지 않은 노드 중에서 가장 최단거리가 짧은 노드를 선택하는 과정을 반복하는 것이 핵심**이다. 또한, 각 단계마다 탐색노드로 한 번 선택된 노드는 최단거리가 갱신되고 난 후 재갱신되지 않는 것을 확인할 수 있다.( 방문처리가 됐기 때문)

```markdown
1. v에서 시작 : distance[v] = 0, visited[v] = 1
2. v에 연결된 노드의 거리 갱신
3. 시작 노드를 제외한 n-1개의 노드중에 방문하지않고 거리값이 가장 작은 노드 차례대로 선택 -> now
4. now에 연결된 노드 거리값 갱신( 더 작은 값으로 )
```



```python
import sys
import heapq
input = sys.stdin.readline
n, m = map(int,input().split())
start = int(input())
INF = int(1e9)
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) 
    distance[start] = 0 
    while q :
        dist, node = heapq.heappop(q)
        if distance[node] < dist: # = 을 붙이게되면 시작 노드일때 continue
            continue
        for after in graph[node]:
            cost = distance[node] + after[1]
            if cost < distance[after[0]]:
                distance[after[0]] = cost
                heapq.heappush(q,(cost,after[0]))

dijkstra(start)

for i in range(1, len(distance)):
    if distance[i] == INF :
        print("도달 불가")
    else :
        print(distance[i])
```

heapq 를 사용해 최소 거리를 구하는 과정과 방문처리 과정을 생략할 수 있었다.
