import sys
input = sys.stdin.readline

n = int(input())
visited = [[-1]*n for _ in range(n)]
graph = [input().rstrip() for _ in range(n)]
def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j: continue # 자신으로 돌아오는 거 제외
                if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] == 'Y') :
                    visited[i][j] = 1

floyd()
ans = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if visited[i][j] == 1 : # 0~n-1 사람이랑 2-친구인 사람이 누구인지 몇명인지
            cnt += 1
    ans = max(ans,cnt)
print(ans)