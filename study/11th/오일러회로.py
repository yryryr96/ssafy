# 오일러 회로가 되려면 간선의 수가 시작,끝점은 홀수이고 나머지는 다 짝수이거나 모두 짝수
# 모든 간선을 돌며 다시 돌아오려면 들어가고 나가는 노드의 개수가 같아야하므로 짝수 개 필요
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
degree = [0]*n

temp = []
for i in range(n):
    lst = {}
    for j,v in enumerate(graph[i]):
        if v:
            lst[j] = 1
            visited[i][j] = v
            degree[i] += v
    temp.append(lst)

for i in range(n):
    if degree[i] % 2 :
        print(-1)
        exit()

ans = []
st = [0]
while st :
    now = st[-1]
    if temp[now] :
        _next = next(iter(temp[now]))
        visited[_next][now] -= 1
        visited[now][_next] -= 1
        degree[now] -= 1
        degree[_next] -= 1

        if not visited[now][_next] :
            del temp[now][_next]
            del temp[_next][now]
        st.append(_next)
    else :
        ans.append(st.pop()+1)

print(' '.join(map(str,ans)))