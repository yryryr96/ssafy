def backtracking(n,m):
    if len(lst) == m :
        print(*lst)
        return

    for i in range(1,n+1):
        if not i in lst:        # 중복 안되게
            lst.append(i)
            backtracking(n,m)
            lst.pop()

lst = []
n, m = map(int,input().split())
backtracking(n,m)