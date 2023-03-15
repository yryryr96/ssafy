# 투 포인터 (Two Pointers)

- 리스트에 순차적으로 접귾래야 할 때 두개의 점 위치를 기록하며 처리하는 알고리즘
- 정렬되어 있는 두 리스트의 합집합에도 사용된다. 병합정렬의 conquer 영역의 기초가 되기도 한다.



```python
# 특정한 합을 가지는 부분 연속 수열 찾기 예제 문제

n,m = 5,5
lst = [1,2,3,2,5]
end = 0
SUM = 0
cnt = 0

for start in range(n): # start 1씩 증가
    while SUM < m and end < n : # s~e 의 부분합이 m보다 작고 end가 n보다 작을 때
        SUM += lst[end]
        end += 1

    if SUM == m :
        cnt += 1
    
    SUM -= lst[start] # start 값이 1 증가할 예정이므로 SUM에서 lst[start] 값을 빼준다.
pritn(cnt) # 부분 연속 수열의 합이 m을 만족하는 개수
```

