

from collections import deque
import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # s가 나올때마다 길이 측정후 길이가 꺾이면 그떄까 최고 길이
    q = deque(sys.stdin.readline().rstrip("\n"))
    ## 방향 키워드를 저장하고 그에 맞는 방향을 미리 구성
    ## 왼쪽일때 넘어가는 방향순서
    ## 오른쪽 방향순서를 기록하여 미리 짜두기
    ## 시계방향 3시방향부터
    ## 오 하 좌 상
    dir = [[0,1],[1,0],[0,-1],[-1,0]]
    ## 각 방향
    dir_R = [0,1,2,3]
    dir_L = [0,3,2,1]
    ans = 0
    ## now는 현재 방향
    k_index = 0
    ## dir
    k = 0
    ## 만약에 L이 나오면 dir_L의 값을 더함
    ## k값을 공유하면서 명령이 나올때 마다 각 방향별 k+1 의 방향을 가져와야됨
    ## 숫자로 방향구하기
    ## 좌회전 우회전을 어떻게 평가할 것인가???
    ### 한 명령을 수행하고 나서 다음 명령을 수행했을때 거리가 더 벌어지면 oo
    ## 명멸한번을 수행하고 거리가 0이면 끝
    loc = [0,0]
    while q:
        x = q.popleft()
        if x == 'S':
            loc[0] += dir[k_index][0]
            loc[1] += dir[k_index][1]
            ## 거리계싼싼
            ans = (loc[0] * loc[0]) + (loc[1]+loc[1])
            print(ans)
        if x == 'L':
            k = dir_L.index(k_index)
            if k + 1 < 4:
                k  += 1
                k_index = dir_L[k]

            elif k+1 >=4:
                k = (k+1) % 4
                k_index = dir_L[k]
        ## 왼쪽만 도는건 됐는데
        if x == 'R':
            k = dir_R.index(k_index)
            if k+1 < 4:
                k+= 1
                k_index = dir_R[k]
            elif k + 1 > 4:
                k = (k+1)%4
                k_index= dir_R[k]

    print(loc)