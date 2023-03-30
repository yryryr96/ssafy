T = int(input())
for tc in range(1, T + 1):
    n, limit = map(int, input().split())
    lst = []
    for _ in range(n):
        score, calorie = map(int, input().split())
        lst.append((score, calorie))

    MAX = 0
    def dfs(idx, s, c):
        global MAX
        if c > limit:
            return
        if s > MAX:
            MAX = s
        for i in range(idx + 1, n):
            dfs(i, s + lst[i][0], c + lst[i][1])
        return
    dfs(-1, 0, 0)
    print(f'#{tc} {MAX}')
