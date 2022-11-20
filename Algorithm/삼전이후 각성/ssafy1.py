## 제발 통괒모 합시다....
## 그만 고통받고 싶어 십라...
# 맨날 떨어졌는데 또 떨어지면 뭐 별차이 있나
## 오늘 할거 영어면접 연습, 티맥스 자소서 보내기 헬스부터 먼저 가야지

T = int(input())
for test_case in range(1, T + 1):
    m,n = map(int,input().split())
    temp = [list(map(int,input().split())) for _ in range(n)]
    points = []
    answer = 0
    for point in temp:
        a,b = point
        points.append([a-1,b-1])
    # print(points)
    # U 명령 갯수
    points = sorted(points, reverse= True)
    # print(points)
    answer += points[0][0]

    ## 좌 우 정렬
    points = sorted(points, key= lambda x : x[1])
    # print(points)
    temp_left = abs(points[-1][1])
    temp_right = abs(points[0][1] - (m-1))
    if temp_right >= temp_left:
        answer += temp_left
    else:
        answer += temp_right
    print("#{} {}".format(test_case, answer))