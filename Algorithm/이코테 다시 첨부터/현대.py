import sys
import math

input = sys.stdin.readline
m = 1000000001
a, b = map(int, input().split())
matrix = [[1000000001] * b for _ in range(b)]
checked = [[0] * b for _ in range(b)]
for _ in range(b):
    i, k, c = map(int, input().split())
    if matrix[i - 1][k - 1] > c:
        matrix[i - 1][k - 1] = c
    if matrix[k - 1][i - 1] > c:
        matrix[k - 1][i - 1] = c


def define(n):
    if n == 1:
        return False
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def dfs(n, end, rate):
    global matrix
    global m
    global checked
    if n == end:
        if rate < m:
            m = rate

    else:
        for i in range(a):
            if matrix[n][i] != 1000000001 and checked[n][i] == 0:
                ## 탐색을 할지말지
                if matrix[n][i] >= m or n == i:
                    continue

                checked[n][i] = 1
                if rate < matrix[n][i]:
                    rate = matrix[n][i]
                dfs(i, end, rate)
                checked[n][i] = 0ㅇ

    return


dfs(0, a - 1, 0)
while True:
    if define(m):

        print(m)
        break
    else:
        m += 1

