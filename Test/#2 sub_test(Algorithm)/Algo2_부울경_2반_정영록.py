T = int(input())    # test case
for tc in range(1,T+1):
    N = int(input())
    r,c = map(int,input().split()) # 망치의 시작 행,열 위치
    lst = [[0 for _ in range(100)] for _ in range(100)] # 100x100 리스트 생성
    score = 0
    for _ in range(N):
        A,B,K = map(int,input().split()) # A,B : 두더지의 좌표, K : 두더지가 몇초동안 유지 되는지
        lst[A][B] = 1
        k = 0 ; n = 0 # k : 가로로 몇번 움직였는지 , n : 세로로 몇 번 움직였는지
        while k < K : # 가로로 움직인 횟수가 K번보다 작을 때
            k += 1
            if c < B :  # 망치의 열의 좌표가 두더지 좌표보다 작다면
                c = c + 1

            elif c > B : # 망치의 열의 좌표가 두더지 좌표보다 크다면
                c = c - 1

            if r==A and c==B :  # 망치가 두더지를 잡았을 때 점수 1점 획득
                score += 1
                break

            if c == B : # K번 내에 열의 좌표가 같아진다면 break 하고 행 좌표 변환
                break

        while n+k < K : # 가로+세로로 움직인 횟수가 K번 보다 작을 때
            n+=1
            if r < A :  # 망치의 행의 좌표가 A보다 작을 때
                r = r + 1

            elif r > A : # 망치의 행의 좌표가 A보다 클 때
                r = r - 1

            if r==A and c==B : # 망치로 두더지를 잡았을 때 점수 획득
                score += 1
                break

    print(f'#{tc} {score}')