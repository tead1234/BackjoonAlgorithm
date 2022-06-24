from collections import deque

def network(i,j,computers,n):
    answer = 0
    visited=set()

    que=deque()
    que.append((i,j))

    while que:
        start,end=que.popleft()
        visited.add(end)

        for i in range(n):
            if computers[end][i]==1:
                if i not in visited:
                    que.append((end,i))

                computers[end][i]=0

def solution(n, computers):
    answer=0

    for i in range(n):
        for j in range(n):
            if computers[i][j]==1:
                network(i,j,computers,n)
                answer+=1

    return answer
print(solution(4, [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]]))