T = int(input())
for tc in range(1,T+1):
    N = int(input())
    check = [0 * N for _ in range(N)]
    board = [0 for _ in range(N)]
    ans = 0

<<<<<<< HEAD
    def nqueen(row):
        global ans
        if row == N:
            ans += 1
            return

        for i in range(N):
            if check[i] == 1:
                continue

            board[row] = i
            promising = True
            for j in range(row):
                if board[row] == board[j] or (row - j == abs(board[row] - board[j])):
                    promising = False
                    break
=======
n,m,h = map(int,input().split())
graph = [[0]*(n+1) for _ in range(h+1)]

def move():
    for j in range(1,n+1):
        col = j
        for row in range(1,h+1):
            if graph[row][col] :
                col += 1
            elif graph[row][col-1] :
                col -= 1
        if col != j :
            return False
    return True

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1

MIN = sys.maxsize
def dfs(row,col,cnt):
    global MIN

    if move():
        MIN = min(MIN,cnt)
        return MIN

    if cnt == 3 or cnt >= MIN:
        return

    for i in range(row,h+1):
        if i == row :
            col = col
        else :
            col = 1
        for j in range(col,n):
            if graph[i][j] == 0 and graph[i][j - 1] == 0 and graph[i][j+1] == 0 :
                graph[i][j] = 1
                dfs(i,j+1, cnt + 1)
                graph[i][j] = 0

dfs(1,1,0)

if MIN > 3 :
    print(-1)

else:
    print(MIN)
>>>>>>> 7fda2b1c8b6e710364915d4baab05d81f5b43386

            if promising:
                check[i] = 1
                nqueen(row + 1)
                check[i] = False
    nqueen(0)
    print(f'#{tc} {ans}')