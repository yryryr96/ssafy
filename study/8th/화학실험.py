import sys
input = sys.stdin.readline

n,k = map(int, input().split())
lst = list(map(int, input().split()))
temp = []
for i in range(k):
    temp.append([lst[i],i+1])

temp.sort(reverse=True)

if max(lst) -1 > sum(lst) - max(lst) :
    print(-1)
    exit()
else:
    ans = [0] * n
    j = 0
    for i in range(0,n,2):
        ans[i] = temp[j][1]
        temp[j][0] -= 1
        if temp[j][0] == 0 :
            j+=1

    i = 1
    while i < n :
        ans[i] = temp[j][1]
        temp[j][0] -= 1
        if temp[j][0] == 0 :
            j += 1
        i+=2

    print(*ans)
