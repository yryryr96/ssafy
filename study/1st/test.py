<<<<<<< HEAD
import heapq,sys
input = sys.stdin.readline

n,m = map(int,input().split())
q = list(map(int,input().split()))
q.sort()
ans = 0
while q :
    A = q.pop()
    temp = A

    if not q :
        ans+=temp
    while A != 0 and q :
        for _ in range(m-1):
            B = q.pop()
            A -= B
            if A == 0 :
                ans += temp
                temp = 0
                break
        if not q:
            ans += temp
            break




print(ans)
=======
# 30의 배수이면 각 자리수의 합이 3의 배수이다.
import sys
input = sys.stdin.readline

numbers = input().rstrip()
num = list(map(int,numbers))

temp = 1

if '0' not in numbers :
    temp = 0

if temp == 0 :
    print(-1)
else :
    if sum(num) % 3 == 0 :
        num.sort(key=lambda x : -x)
        num = list(map(str,num))
        print(''.join(num))
    else:
        print(-1)
>>>>>>> 19d542a36b75442d05050a6444f066effcf82a7e
