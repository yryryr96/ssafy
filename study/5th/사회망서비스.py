import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]

#내가 EA 가 아닐때와 EA일 때 구분
# 아닐 때 EA 수, EA일때 EA 수
dp = [[0,1] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)

def dfs(now):
    # 시작 지점은 상관 없지만 방문한 곳 다시 방문은 x
    visited[now] = 1 # 현재 노드

    for child in graph[now] : # 현재 노드의 자식 child
        if not visited[child] :
            dfs(child)  # leaf node 까지 탐색

            dp[now][0] += dp[child][1]
            # 내가 얼리어답터가 아니면 자식은 무조건 얼리어답터여야 함

            dp[now][1] += min(dp[child][0],dp[child][1])
            # 내가 얼리어답터라면 자식이 얼리어답터든 아니든 상관없으니 그냥 작은값 더해주기

dfs(1)

print(min(dp[1][0],dp[1][1]))
