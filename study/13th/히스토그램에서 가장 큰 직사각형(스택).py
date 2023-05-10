import sys
input = sys.stdin.readline

while True :
    n,*histogram = list(map(int,input().split()))
    if not n :
        break

    st = []
    ans = 0
    histogram.append(0)
    # 마지막에 스택에 남은 애들 다 계산해주기 위해서 0 추가
    for idx,h in enumerate(histogram) :
        # print(idx,h)
        while st and histogram[st[-1]] > h :
            H = histogram[st.pop()]
            if st : W = idx - st[-1] - 1
            else : W = idx
            ans = max(H*W,ans)
        st.append(idx)

    print(ans)