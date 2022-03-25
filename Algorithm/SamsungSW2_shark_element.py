
from collections import deque

import sys

N = int(sys.stdin.readline())
queue = deque()
queueForSorting = deque()
인접행렬 = [list(map(int, sys.stdin.readline().split())) for i in range(N * N)]
좋아하는행렬 = [[0] * 4 for i in range(N * N)]
graph = [[0] * N for i in range(N)]
COUNT_0 = 0
COUNT_1 = 0
HappyScore = 0
k = 0
c= 0
MAX_0 = 0
MAX_1 = 0
MIN_i = N
MIN_j = N
for i in range(N*N):
    for j in range(1, 5):
        좋아하는행렬[i][j - 1] = 인접행렬[i][j]

for i in range(N * N):
    queue.append(인접행렬[i][0])

queue2 = queue.copy()

while (True):
    if queue:
        학생 = queue.popleft()

        for i in range(N):
            for j in range(N):
                if graph[i][j] == 0:
                    if i - 1 >= 0:
                        if graph[i - 1][j] == 0:
                            COUNT_0 += 1
                        elif graph[i - 1][j] in 좋아하는행렬[k]:
                            COUNT_1 += 1
                    if j - 1 >= 0:
                        if graph[i][j - 1] == 0:
                            COUNT_0 += 1
                        elif graph[i][j - 1] in 좋아하는행렬[k]:
                            COUNT_1 += 1
                    if j + 1 < N:
                        if graph[i][j + 1] == 0:
                            COUNT_0 += 1
                        elif graph[i][j + 1] in 좋아하는행렬[k]:
                            COUNT_1 += 1
                    if i + 1 < N:
                        if graph[i+1][j] == 0:
                            COUNT_0 += 1
                        elif graph[i+1][j] in 좋아하는행렬[k]:
                            COUNT_1 += 1

                    else:
                        pass

                    if MAX_1 < COUNT_1:
                        MAX_1 = COUNT_1
                        MAX_0 = COUNT_0
                        예상자리 = (i,j)
                    if MAX_1 == COUNT_1:
                        if MAX_0 < COUNT_0:
                            MAX_0 = COUNT_0
                            예상자리 = (i,j)
                        elif MAX_0 == COUNT_0:
                            # 최소 i 그다음 최소 j
                            if MIN_i > i:
                                MIN_i = i
                                MIN_j = j
                                예상자리 = (i, j)
                            if MIN_i == i:
                                if MIN_j > j:
                                    MIN_j = j
                                    예상자리 = (i,j)
                COUNT_0 = 0
                COUNT_1 = 0

        k += 1
        graph[예상자리[0]][예상자리[1]] = 학생

        예상자리 = (0,0)
        MAX_1 = 0
        MAX_0 = 0
        MIN_j = N
        MIN_i = N
    else:
        break


while(queue2):
    행복도학생 = queue2.popleft()
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 행복도학생:
                if i - 1 >= 0:
                    if graph[i - 1][j] in 좋아하는행렬[c]:
                        COUNT_1 += 1
                if j - 1 >= 0:
                    if graph[i][j - 1] in 좋아하는행렬[c]:
                        COUNT_1 += 1
                if j + 1 < N:
                    if graph[i][j + 1] in 좋아하는행렬[c]:
                        COUNT_1 += 1
                if i + 1 < N:
                    if graph[i + 1][j] in 좋아하는행렬[c]:
                        COUNT_1 += 1
                else:
                    pass

            if COUNT_1 == 1:
                HappyScore += 1
            elif COUNT_1 == 2:
                HappyScore += 10
            elif COUNT_1 == 3:
                HappyScore += 100
            elif COUNT_1 == 4:
                HappyScore += 1000

            COUNT_1 = 0
    c+= 1
print(HappyScore)
