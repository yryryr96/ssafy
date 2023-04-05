import sys
from itertools import permutations
input = sys.stdin.readline

n,k = map(int,input().split())
lst = list(map(int,input().split()))
temp = []
for i in range(len(lst)) :
    for j in range(lst[i]) :
        temp.append(i+1)
print(temp)
for p in permutations(temp,n):
    temp = 1
    for i in range(1,n-1):
        if p[i-1] == p[i] or p[i] == p[i+1] :
            temp = 0
            break
    if temp == 1:
        print(*p)
        break
else:
    print(-1)
