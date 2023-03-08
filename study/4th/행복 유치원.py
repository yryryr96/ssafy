import sys
input = sys.stdin.readline

N,K = map(int,input().split())
lst = list(map(int,input().split()))
ans = [0]*(N-1)
for i in range(N-1):
    ans[i] = lst[i+1] - lst[i]

ans.sort()
ANS = 0
for n in range(N-K):
    ANS += ans[n]
print(ANS)

# 작은 키차이들만 (N-K)개 선택해서 더해준다.