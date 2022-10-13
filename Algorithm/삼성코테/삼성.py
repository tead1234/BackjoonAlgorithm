T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    building = list(map(int,input().split()))
    answer = 0
    flg = False
    for k in range(2,N-2):
        ## 좌우 탐색
        flg = False
        for i in range(1,3):
            if building[k+i] > building[k]:
                flg =True
                break
        for j in range(1,3):
            if building[k- j] > building[k]:
                flg =  True
                break
        ## 둘다 안걸렸다면  가장 높은 애를 찾아서 차이를 구하고
        if flg:
            continue

        ## 빅을 빠르게 바꿀수 있는 방법법
        big = max([building[k-2],building[k-1],building[k+1],building[k+2]])
        answer += (building[k] - big)

    print("#{} {}".format(test_case, answer))
