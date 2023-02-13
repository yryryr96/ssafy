# boj.1966 (프린터큐) 아직 못품

```python
import sys
from collections import deque

T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    P = list(map(int,input().split()))
    lst = list(range(1,N+1))
    lst[M] = 'A'
    cnt = 0
    while lst:
        print(lst)
        print(P)

        if P[lst[0]] == max(P) :
            P.pop(lst.pop(0))
            cnt+=1

        else :
            lst.append(lst[0])
            cnt += 1
```

