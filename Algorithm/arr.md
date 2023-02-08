# 2차원 배열
- ##  델타를 이용한 2차 배열 탐색
```python
arr[0...N-1][0...N-1] # NxN 배열
di[] = [0, 0, -1, 1] # 상하
dj[] = [-1, 1, 0, 0] # 좌우

for i : 0 -> N-1
    for j : 0 -> N-1 :
        for k in range(4) :
            ni <- i + di[k]
            nj <- j + dj[k]
            if 0 <= < N and 0 <= nj < N # 유효한 인덱스면
                test(arr[ni][nj])
```
```python
di = [0,1,0,-1]
dj = [1,0,-1,0]

#1
N = 3
for i in range(N) :
    for j in range(N):
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0<=ni<N and 0<=nj<N :
                print(i,j,ni,nj)
#2
N = 3
for i in range(N) :
    for j in range(N):
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]] :
            ni = i+di ; nj = j+dj
            if 0<=ni<N and 0<=nj<N :
                print(i,j,ni,nj)
```

- ## 부분집합 생성하기
    - 집합의 원소가 n개일 때, 공집합을 포함한 부분집합 수는 2^n개이다.

```python
A = [1,2,3,4]
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] =  i                 # 0번째 원소
    for j in range(2):
        bit[1] = j              # 1번째 원소
        for k in range(2):
            bit[2] = k          # 2번째 원소
            for l in range(2):
                bit[3] = l      # 3번재 원소
                print(bit)   # 생성된 부분집합 출력
                for p in range(4):
                    if bit[p] : 
                        print(A[p], end = ' ')
                print()
```
- ## 비트 연산자
```python
arr = [3,6,7,1,5,4]

n = len(arr)

for i in range(1<<n) :          #  1<<n : 부분 집합의 개수
    for j in range(n) :         # 원소의 수만큼 비트를 비교함
        if i & (1<<j) :         # i의 j번 비트가 1인 경우
            print(arr[j], end = ",") # j번 원소 출력
    print()
print()
```

- ## 달팽이 배열

```python
def snail_board(n):
    board = [[0] * n for _ in range(n)]

    trans = 1
    cnt = 1
    row, col = 0, -1

    while n > 0:
        for i in range(n):  # ->, <- (col)
            col += trans
            board[row][col] = cnt
            cnt += 1

        n -= 1		# 첫 번째 외 2번씩 같은 칸 수 이동

        for i in range(n):  # 아래, 위 (row)
            row += trans
            board[row][col] = cnt
            cnt += 1

        trans *= -1	  # 증가/감소 방향 변경

    return board

T=int(input())
for tc in range(1,1+T):
    n = int(input())
    print(f'#{tc}')
    for i in range(n):
        for j in range(n):
            print(snail_board(n)[i][j],end=' ')
        print()
```

