import sys,heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
<<<<<<< HEAD
    max_heap = []
    min_heap = []
    visited = [0]*k
    for id in range(k):
=======
    q1 = []
    q2 = []
    cnt = 0
    for _ in range(k):
>>>>>>> f38c0029d6f492e4db3fbbf95e54937a6467d1a0
        command,num = input().rstrip().split()
        num = int(num)

        if command == 'I' :
<<<<<<< HEAD
            heapq.heappush(max_heap,(-num,id))
            heapq.heappush(min_heap,(num,id))
            visited[id] = 1

        else:
            if num == - 1:
                while min_heap and not visited[min_heap[0][1]] :
                    heapq.heappop(min_heap)
                if min_heap :
                    visited[min_heap[0][1]] = 0
                    heapq.heappop(min_heap)

            elif num == 1 :
                while max_heap and not visited[max_heap[0][1]] :
                    heapq.heappop(max_heap)
                if max_heap :
                    visited[max_heap[0][1]] = 0
                    heapq.heappop(max_heap)

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap :
        print('EMPTY')
    else:
        print(-max_heap[0][0],min_heap[0][0])
=======
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
>>>>>>> f38c0029d6f492e4db3fbbf95e54937a6467d1a0
