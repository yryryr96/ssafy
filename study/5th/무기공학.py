import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
point = [[0,1],[0,1],[0,-1],[-1,0]]

