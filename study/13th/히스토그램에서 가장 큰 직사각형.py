import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def init(node,start,end):
    if start == end :
        tree[node] = (histogram[start], start)
        return tree[node]

    else :
        left = init(node*2, start, (start+end)//2)
        right = init(node*2+1, (start+end)//2 + 1, end)

        if left[0] < right[0] :
            tree[node] = left
        else :
            tree[node] = right
        return tree[node]

def calc(node,start,end,left,right) :
    global MAX
    if left > end or right < start :
        return (sys.maxsize,0)

    if left <= start and end <= right :
        return tree[node]

    left_tree = calc(node*2,start,(start+end)//2,left,right)
    right_tree = calc(node*2+1,(start+end)//2+1,end,left,right)

    if left_tree[0] < right_tree[0] :
        return left_tree
    else:
        return right_tree

def solution(left,right):
    if left == right :
        return histogram[left]

    min_h, idx = calc(1,0,n-1,left,right)
    s1,s2,s3 = min_h * (right - left + 1), 0, 0
    if idx - 1 >= left :
        s2 = solution(left, idx-1)
    if idx + 1 <= right :
        s3 = solution(idx+1,right)

    return max(s1,s2,s3)

while True :
    MAX = 0
    histogram = list(map(int,input().split()))
    n = histogram[0]
    tree = [0]*(4*n)
    if n == 0 :
        break
    histogram = histogram[1:]
    init(1,0,n-1)
    print(solution(0,n-1))