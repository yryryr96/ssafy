# boj.1654 (랜선 자르기) - 이분 탐색

```python
K,N = map(int,input().split())
lst = []
for _ in range(K):
    n = int(input())
    lst.append(n)
end = sum(lst)//N   # 최대 길이
start = 1           # 최소 길이
middle = (start + end) // 2

while start <= end:     # 이분 탐색 완료 조건

    middle = (start + end) // 2 # 최대 길이 최소 길이 중간값
    SUM = 0 # 랜선 수

    for k in lst:   # 랜선을 자른 수
        SUM += k//middle

    if SUM < N:     # 랜선을 자른 수가 만들어야될 랜선의 수보다 작을 때
        end = middle - 1    # 랜선의 최대 길이를 중간값보다 1 작게 설정

    if SUM >= N:    # 랜선을 자른 수가 만들어야될 랜선의 수보다 클 때
        start = middle + 1  # 랜선의 최소 길이를 중간값보다 1 크게 설정

print(end) # 왜 end를 출력하는지 생각해볼 것
```



