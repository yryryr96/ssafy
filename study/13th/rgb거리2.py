import sys
input = sys.stdin.readline

n = int(input())
rgb = [list(map(int,input().split())) for _ in range(n)]
ans = sys.maxsize
for k in range(3) :
    dp = [[sys.maxsize] * 3 for _ in range(n)]
    dp[0][k] = rgb[0][k] # 처음 색깔 선택 k
    for i in range(1,n):
        dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + rgb[i][0]
        dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + rgb[i][1]
        dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + rgb[i][2]

    for j in range(3):
        if j!=k :   # 마지막 색이 첫 색이랑 다르다면
            ans = min(ans,dp[n-1][j])

print(ans)
