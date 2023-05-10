import sys
input = sys.stdin.readline

line = []
n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    line.append((a,b))

line.sort()
start = end = -sys.maxsize
ans = 0
for x,y in line :
    if end < x :
        ans += (end - start)
        start = x
        end = y


    elif x >= start and y >= end :
        end = y

    elif x >= start and y <= end :
        continue

ans += (end-start)
print(ans)