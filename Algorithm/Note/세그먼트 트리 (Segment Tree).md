# 세그먼트 트리 (Segment Tree)

```python
# boj 2042 
import sys, heapq
input = sys.stdin.readline

# 트리 초기화
def init(node, start, end):
    if start == end :
        tree[node] = l[start]
        return tree[node]
    else :
        tree[node] = init(node*2, start, (start+end)//2) + init(node*2+1,(start+end)//2+1,end)
        return tree[node]

# 구간 합
def subSum(node,start,end,left,right):
    if left > end or right < start :
        return 0

    if left <= start and end <= right :
        return tree[node]

    return subSum(node*2, start, (start+end)//2, left, right) + subSum(node*2+1, (start+end)//2 + 1, end,left,right)

# 세그먼트 트리 업데이트 , 특정 값이 바뀌면 그 값과 연관된 트리의 값들도 모두 바껴야 함
def update(node, start, end, index, diff):
    if index < start or index > end :
        return

    tree[node] += diff

    if start != end :
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2+1, (start+end)//2+1,end, index, diff)

n,m,k = map(int,input().split())
l = [0]
tree = [0]*3000000

for _ in range(n):
    l.append(int(input()))

init(1,1,n)

for _ in range(m+k):
    a,b,c = map(int,input().split())

    if a == 1 :
        diff = c - l[b]
        l[b] = c
        update(1,1,n,b,diff)
    else :
        print(subSum(1,1,n,b,c))
```

