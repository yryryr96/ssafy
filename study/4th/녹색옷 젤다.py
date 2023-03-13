# 다익스트라 2차원 버전
import sys
import heapq
input = sys.stdin.readline
tc = 1
while True:

    n = int(input())
    if n == 0 :
        break

    INF = int(1e9)
    graph = [list(map(int,input().split())) for _ in range(n)]  # 가중치 그래프라고 생각
    distance = [[INF]*(n) for _ in range(n)]    # 2차원 거리 리스트 생성
    def dijkstra():
        q = []
        point = [[0,1],[1,0],[-1,0],[0,-1]] # 좌표 탐색 델타
        heapq.heappush(q,(graph[0][0],(0,0))) # q에 가중치, 좌표 push
        distance[0][0] = graph[0][0]        # 시작 좌표 거리 초기화
        while q:
            dist, node = heapq.heappop(q)   # 거리, 좌표값

            if node == (n-1,n-1) :
                print(f'Problem {tc}: {distance[n-1][n-1]}')
                return

            if distance[node[0]][node[1]] < dist :  # 조사한 거리보다 이미 더 작은 값이 들어와있다면 패스
                continue

            for di,dj in point :
                ni,nj = node[0] + di, node[1] + dj
                if 0<=ni<n and 0<=nj<n :    # 상하좌우 조사해서 범위 안에 있으면
                    cost = distance[node[0]][node[1]] + graph[ni][nj]   # 현재까지 거리 값에 다음 조사할 가중치 더한 값

                    if cost < distance[ni][nj]: # 작은 값으로 갱신하고 q에 push
                        distance[ni][nj] = cost
                        heapq.heappush(q,(cost,(ni,nj)))

    dijkstra()
    tc += 1

