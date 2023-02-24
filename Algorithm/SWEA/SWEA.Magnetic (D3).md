```python
# 1. 그래프의 좌표가 1이면 밑으로 2면 위로 간다는 뜻이니까 한쪽만 고려하면 된다고 생각
# 2. 1일 때 밑으로 가며 2를 만나면 교착상태 + 1
# 3. 1일 때 밑으로 가며 1을 만나면 어짜피 같은 자성체라고 생각해 해당 좌표를 0으로 변경

for tc in range(1,11):
    N = int(input())
 
    graph = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    for j in range(N):
        for i in range(N):
            if graph[i][j] == 1 :			# 좌표값이 1일 때
                for k in range(i+1,N):	# 0번째 열부터 밑으로 탐색
                    if graph[k][j] == 1:	# 1을 만나면 0으로 변경
                        graph[k][j] = 0
                    elif graph[k][j] == 2 :	# 2를 만나면 교착상태를 형성하므로 + 1 해주고 멈춤
                        cnt += 1
                        break
 
    print(f'#{tc} {cnt}')
```

