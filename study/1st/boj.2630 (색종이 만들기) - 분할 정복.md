# boj.2630 (색종이 만들기) - 분할 정복

```python
N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
ans = []
def div(i,j,N):

    color = graph[i][j]
    for k in range(i,i+N):		# 범위 주의!!
        for n in range(j,j+N):	# 범위 주의!!
            if graph[k][n] != color :
                div(i,j,N//2)
                div(i,j+N//2,N//2)
                div(i+N//2,j,N//2)
                div(i+N//2,j+N//2,N//2)
                return
    if  color == 0 :
        ans.append(0)
    else :
        ans.append(1)

div(0,0,N)

print(ans.count(0))
print(ans.count(1))
```

