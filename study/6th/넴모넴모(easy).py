# pypy로 제출
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[0]*(m+1) for _ in range(n+1)]
ans = 1

def dfs(i,j):
    global ans
    if j == m+1 :   # 열 끝으로 이동하면 행,열 좌표 이동
        i += 1
        j = 1

    if i == n+1 :   # 행이 끝까지 넘어가면 리턴
       return 0

    if graph[i][j-1] == 0 or graph[i-1][j] == 0 or graph[i-1][j-1] == 0 :
        #오른쪽 아래 좌표 기준 네모가 아니라면
        graph[i][j] = 1
        ans += 1
        dfs(i,j+1)
        graph[i][j] = 0

    dfs(i,j+1)
    # 네모이면 다음 좌표 탐색
    return

dfs(1,1)
print(ans)