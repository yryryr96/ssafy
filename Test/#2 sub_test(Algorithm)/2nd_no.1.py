T = int(input())    # test case
for tc in range(1,T+1):
    N,M = map(int,input().split())

    lst = [[0 for _ in range(N)] for _ in range(N)] # NxN 배열 리스트 생성 , 0으로 초기화
    cnt = 0
    for _ in range(M): # M 번 반복하여 색칠
        y,x,b,h = map(int,input().split()) # y좌표, x좌표, b 넓이 ,h 높이

        for i in range(y,y+h):
            for j in range(x,x+b):
                lst[i][j] = 1   # 색칠된 부분을 1로 표시

    for i in range(N):
        for j in range(N):
            if lst[i][j] == 1:
                cnt += 1    # 1의 개수가 넓이

    print(f'#{tc} {cnt}')