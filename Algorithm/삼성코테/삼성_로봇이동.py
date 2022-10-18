

from collections import deque


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # s가 나올때마다 길이 측정후 길이가 꺾이면 그떄까 최고 길이
    s = input()
    q= deque(s)

    dir = [[0,1],[1,0],[0,-1],[-1,0]]
    ## 각 방향
    dir_R = [0,1,2,3]
    dir_L = [0,3,2,1]
    ans = 0
    MAXans = []
    ## now는 현재 방향
    k_index = 0
    ####
    ## dir
    k = 0
    cnt = 0

    loc = [0,0]
    MAXofTurn = 0
    while q:
        x = q.popleft()
        if x == 'S':
            loc[0] += dir[k_index][0]
            loc[1] += dir[k_index][1]
            ## 거리계싼싼


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
            elif k + 1 >= 4:
                k = (k+1)%4
                k_index= dir_R[k]
        ans = (loc[0] * loc[0]) + (loc[1] * loc[1])
        print(k_index)
        print(k)
        MAXans.append(ans)
        if len(q) == 0:
            print(loc)
            q += s
            if MAXofTurn >= max(MAXans):
                cnt += 1
                break
            elif MAXofTurn < max(MAXans) and cnt <5:
                MAXofTurn = max(MAXans)
                MAXans = []
                cnt += 1
            elif cnt >=5:
                MAXofTurn = 'oo'

                break



    print("#{} {}".format(test_case, MAXofTurn))