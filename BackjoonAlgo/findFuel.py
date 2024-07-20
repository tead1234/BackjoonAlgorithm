import sys
from collections import deque


## 완탐?
def solution(land):
    answer = 0

    for n in range(len(land[0])):

        if instrument(land, n) > answer:
            answer = instrument(land, n)

    return answer


def instrument(land, n):
    acc = 0
    for idx, l in enumerate(land):
        if l[n] == 1:
            acc += findGasoline(land, idx, n)
    return acc


## 입력받은 map에서
def findGasoline(land, x, y):
    q = deque((x, y))
    visited = [(x, y)]
    Acc = 0
    max_hang = len(land)
    max_yeol = len(land[0])
    adjustment = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        a = q.popleft()
        print(a)
        next_x = a[0]
        next_y = a[1]
        if land[next_x][next_y] == 1:
            Acc += 1
            ## 사방이 유효한 값이면 후보에 넣기
            for ad in adjustment:
                if max_hang > next_x + ad[0] >= 0 and max_yeol > next_y + ad[1] >= 0:
                    q.append((next_x + ad[0], next_y + ad[1]))
    return Acc


solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]])