import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dp = [[1,0] for _ in range(n+1)] # 노드값, 가중치
for _ in range(m):
    s,e,w = map(int,input().split())

    if w >= 7 : # 대기시간이 7일 이상이면 재접종 1일 더하기
        w += 1

    dp[s][1] = w
    if dp[s][0] == 1 :  # 그 노드의 값이 1 즉, 1일차에 접종된다면
        if dp[e][0] <= w :  # e노드의 값과 s노드의 가중치값과 비교해서 더 큰 값 대입
            dp[e][0] = w + 1

    else : # 1일차 접종이 아니라면 s노드의 값과 가중치를 더한값과 e노드의 값과 비교
        if dp[e][0] <= dp[s][1] + dp[s][0] :
            dp[e][0] = dp[s][0] + dp[s][1]

MAX = 0
for i in range(n+1):
    if dp[i][0] > MAX :
        MAX = dp[i][0]
print(MAX)