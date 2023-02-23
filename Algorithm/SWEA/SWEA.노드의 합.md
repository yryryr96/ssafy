# SWEA.노드의 합

```python
T = int(input())
for tc in range(1,T+1):
    N,M,L = map(int,input().split())
    heap = [0] * (N + 1)
    for _ in range(M):
        ci,c = map(int,input().split())

        heap[ci] = c

    k = N//2
    while k != 0 :
        k = N // 2
        heap[k] += heap[N]
        N -= 1
    ans = heap[L]
    print(f'#{tc} {ans}')

```

