

from collections import deque
import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # s가 나올때마다 길이 측정후 길이가 꺾이면 그떄까 최고 길이
    q = deque(sys.stdin.readline().rstrip("\n"))
    dx = [-1,0,1,0]
    dy = [0,-1,0 ,1]
    k = 0
    ## 숫자로 방향구하기
    loc = [0,0]
    while q:
        x = q.popleft()
        if x == 'S':

