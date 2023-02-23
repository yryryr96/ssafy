# SWEA.1232 (사칙 연산)

```python
for tc in range(1,11):
    N = int(input())
    tree = [0]*(N+1)
    left = [0]*(N+1)
    right = [0]*(N+1)

    for _ in range(N):
        s = input().split()
        tree[int(s[0])] = s[1]

        if len(s) == 4:
            left[int(s[0])] = int(s[2])
            right[int(s[0])] = int(s[3])

    def post(v):
        if v:
            post(left[v])
            post(right[v])

            if tree[v] == '+' :
                tree[v] = int(tree[left[v]]) + int(tree[right[v]])
            elif tree[v] == '-':
                tree[v] = int(tree[left[v]]) - int(tree[right[v]])
            elif tree[v] == '/':
                tree[v] = int(tree[left[v]]) // int(tree[right[v]])
            elif tree[v] == '*' :
                tree[v] = int(tree[left[v]]) * int(tree[right[v]])
        return

    post(1)
    print(f'#{tc} {tree[1]}')
```

