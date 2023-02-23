# SWEA.이진 힙

```python
# min heap

def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c//2

    while p > 0 and heap[p] > heap[c] :
        heap[c],heap[p] = heap[p],heap[c]
        c = p
        p = c//2

    return


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    par = [0] * (N + 1)
    heap = [0]*501
    last = 0
    lst = list(map(int,input().split()))

    while lst :
        enq(lst.pop(0))
    SUM = 0
    k = N
    while k != 1 :
        k //= 2
        SUM += heap[k]

    print(f'#{tc} {SUM}')
```

