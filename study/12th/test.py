import sys
input = sys.stdin.readline

def init(node,start,end) :
    if start == end :
        tree[node] = numbers[start]
        return tree[node] % 1000000007
    else :
        left = init(node*2, start, (start+end)//2)
        right = init(node*2+1, (start+end)//2 + 1, end)
        tree[node] = left*right
        return tree[node] % 1000000007

def multi(node,start,end,left,right):
    if start > right or end < left :
        return 1

    if left <= start and end <= right :
        return tree[node] % 1000000007

    return (multi(node*2,start,(start+end)//2,left,right) * multi(node*2+1, (start+end)//2 + 1, end, left,right)) % 1000000007

def update(node,start,end,index, diff) :
    if index < start or index > end :
        return
    # print(index)
    # print(numbers[index])
    if start == end :
        tree[node] = diff
        return

    if start != end :
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2+1, (start+end)//2 + 1, end, index, diff)
        tree[node] = (tree[node*2] * tree[node*2+1]) % 1000000007

n,m,k = map(int,input().split())
numbers = []
tree = [0]*(4*n)
for _ in range(n):
    numbers.append(int(input()))

init(1,0,n-1)
for _ in range(m+k):
    a,b,c = map(int,input().split())
    if a == 1 :
        b -= 1
        diff = c
        update(1,1,n,b+1,diff)
        numbers[b] = c

    else :
        print(multi(1,1,n,b,c))

