# boj.17298 오큰수

```python
from collections import deque
import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = list(map(int,input().split()))
st = []			# lst의 인덱스 값을 저장해두고 비교하기위해 사용
ans = [-1]*N

for i in range(N):
    if not st :
        st.append(i)
    else:
        while st and lst[st[-1]] < lst[i] :
            ans[st.pop()] = lst[i]
        st.append(i)

print(*ans)
```

