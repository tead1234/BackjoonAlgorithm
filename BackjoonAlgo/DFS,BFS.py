import sys
#입력받은 숫자와 관계로 인접리스트 구현하기
a,b,c = map(int,input().split())
data = [[map(int, sys.stdin.readline().split())] for _ in range(b)]
data[0][0]
for i in data:
    if data[i][0] == 1:

'''graph = [
        [],
        [4,3,2], #1
        [1,4], #2
        [1,4], #3
        [2,3,1]
        ]
# 정렬을 해야지 제대로 나옴

visited = [False] * len(graph)
# visited가 false의 갯수는 그래프 전체 점 수보다 false가 작거나 같기떄문에
def Dfs(graph,v,visited):
    visited[v] =True
    print(v)
    for i in graph[v]: # v는 시작 줄을 의미, i는 시작줄의 첫 숫자
        if visited[i]==False:
            visited[i] = True
            Dfs(graph,i,visited)

Dfs(graph,1,visited)
'''