T = int(input())
for tc in range(1,T+1):
    N = int(input())
    check = [0 * N for _ in range(N)]
    board = [0 for _ in range(N)]
    ans = 0

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

            if promising:
                check[i] = 1
                nqueen(row + 1)
                check[i] = False
    nqueen(0)
    print(f'#{tc} {ans}')