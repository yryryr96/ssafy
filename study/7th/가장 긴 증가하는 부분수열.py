import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
MAX = 0
for i in range(n-1):
    cnt = 0
    a = lst[i]
    for j in range(i+1,n) :
        if a < lst[j] :
            a = lst[j]
            cnt += 1
    if MAX < cnt :
        MAX = cnt
print(MAX)
