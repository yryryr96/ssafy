# SWEA 계산기3 (D4)

```python
for tc in range(1,11):
    t = int(input())
    words = input()
    pr = {'*': 2 , '/' : 2, '+' : 1, '-': 1 , '(' : 0 }
    st = []
    ans = []
    final = []
    for word in words : 
        if word.isdigit():	# 피연산자일 때
            ans.append(word)
        elif word == '(' :	# 넣을때는 그냥 넣기 우선순위 1순위
            st.append(word)
        elif word == ')':	# ')' 이면 '(' 가 나올때까지 ans.append(st.pop())
            while True:		
                ans.append(st.pop())
                if st[-1] == '(':	# '(' 도 삭제
                    st.pop()
                    break
        else:	# 연산자일 때
            while st and pr[word] <= pr[st[-1]] : 
	# 현재 연산자보다 스택의 연산자 우선순위가 낮아질때까지 ans.append(st.pop())
                ans.append(st.pop())
            st.append(word)

    while st:
        ans.append(st.pop())

    while ans:
        if ans[0] in '+*' :
            b = int(final.pop())
            a = int(final.pop())
            if ans[0] == '+':
                final.append(b+a)
            else :
                final.append(a*b)
            ans.pop(0)
        else :
            final.append(ans.pop(0))

    print(f'#{tc}',*final)

```

괄호 안이라도 연산자 우선순위는 적용

계산은 pop 된거 두개로 연산해서 final 에 push 반복~