K,N = map(int,input().split())
lst = []
for _ in range(K):
    n = int(input())
    lst.append(n)
end = sum(lst)//N   # N개의 랜선으로 나눌 수 있는 최대 길이
start = 1
middle = (start + end) // 2

while start <= end: # 이분 탐색

    middle = (start + end) // 2
    SUM = 0

    for k in lst:   # 나눈 랜선 갯수
        SUM += k//middle

    if SUM < N:
        end = middle -1

    if SUM >= N:    # 최대 길이를 찾기때문에 같을때도 고려해줌
        start = middle + 1

print(end)