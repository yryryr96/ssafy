# SWEA. 진기의 최고급 붕어빵 - 미해결

```python
T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int,input().split())
    lst = list(map(int,input().split()))
    wait = [0]*11112
    i = 1
    while i*M < 11112:
        wait[i*M] = K
        i+=1

    temp =1

    for n in lst:
        if n%2 == 0 :
            if sum(wait[1:n+1]) == 0 :
                temp = 0
                break
            else :
                wait[n] -= 1

        else:
            if sum(wait[1:n]) == 0:
                temp = 0
                break
            else :
                wait[n-1] -= 1

    if temp == 0 :
        print(f"#{tc} Impossible")
    else :
        print(f"#{tc} Possible")
```

