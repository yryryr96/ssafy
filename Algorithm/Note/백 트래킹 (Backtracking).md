# 백 트래킹 (Backtracking)

- 해를 찾아가는 도중, 지금의 경로가 해가 될 것 같지 않으면 그 경로를 더 이상 가지 않고 되돌아가서 다시 해를 찾아 가는 기법 -> 반복문의 횟수를 줄 일 수 있어 효율적
- 일반적으로, 불필요한 경로를 조기에 차단할 수 있게 되어 경우의 수가 줄어들지만 만약 N!의 경우의 수를 가진 문제에서 최악의 경우에는 여전히 지수 함수 시간을 필요로 하므로 처리가 불가능 할 수도 있다.
- 주로 문제 풀이에서는 DFS 등으로 모든 경우의 수를 탐색하는 과정에서, 조건문 등을 걸어 답이 절대로 될 수 없는 상황을 정의하고, 그러한 상황일 경우에는 탐색을 중지시킨 뒤 그 이전으로 돌아가서 다시 다른 경우를 탐색 하게끔 구현

```python
# 백트래킹 연습문제 (boj 15659 : N 과 M(1))

N, M = map(int,input().split())
ans = []

def back():
    if len(ans) == M:
        print(' '.join(map(str,ans)))
        return

    else :
        for i in range(1,N+1):
            if i not in ans:	# 중복된 숫자를 제외하기위해
                ans.append(i)	# 없다면 ans에 추가
                back()			# len(ans) == M이 만족하기 전까지 위 과정 반복
                ans.pop()		
                # len(ans) == M을 만족하고 전 단계로 돌아가서 위 과정을 반복하기 위해 pop()
back()
# 12 13 14 21 23 24 31 32 34 41 42 43
```

```python
# 백트래킹 연습문제 (boj 15650 : N과 N(2))

N, M = map(int,input().split())
ans = []
st = []

def back(n):
    if len(ans) == M:
        print(' '.join(map(str,ans)))
        return

    else:
        for i in range(n,N+1):
            if i not in ans:
                ans.append(i)
                back(i+1)	# 오름차순 정렬 / back(i) 해도 결과 같게 나옴
                ans.pop()

back(1)
# 12 13 14 23 24 34
```

