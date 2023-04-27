import sys,heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    q1 = []
    q2 = []
    cnt = 0
    for _ in range(k):
        command,num = input().rstrip().split()
        num = int(num)

        if command == 'I' :
            cnt += 1
            heapq.heappush(q1,num)
            heapq.heappush(q2,-num)

        if command == 'D' :
            if cnt and num == -1 :
                q2.remove(-heapq.heappop(q1))
                heapq.heapify(q2)
                cnt -= 1
            elif cnt and num == 1 :
                q1.remove(-heapq.heappop(q2))
                heapq.heapify(q1)

                cnt -= 1
            else :
                continue

    if cnt == 0 :
        print('EMPTY')
    else :
        print(-heapq.heappop(q2), heapq.heappop(q1))
