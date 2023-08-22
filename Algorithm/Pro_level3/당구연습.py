def transfer(x, y, m, n):
    return (abs(y - n), x)


def solution(m, n, startX, startY, balls):
    # 결국 원쿠션 때리는 위치가 어디인가가 포인트
    answer = []
    # 좌표 변환
    new_start = transfer(startX, startY, m, n)
    print(new_start)
    new_balls = [transfer(ball[0], ball[1], m, n) for ball in balls]
    print(new_balls)

    ## 벽에 대해서 대칭 후 거리 계산
    for new_ball in new_balls:
        pre = []
        x, y = new_ball
        z, w = new_start
        excepting = 0
        if x == z and y > w:
            excepting = 2
        elif x == z and w > y:
            excepting = 1
        elif y == w and x > z:
            excepting = 3
        else:
            excepting = 0
            ##  좌, 상, 우, 하
        test = [(z, -w), (-w, z), ((n - z) + n, w), (z, (m - w) + m)]
        for idx, t in enumerate(test):
            if idx == excepting:
                continue

            print((abs(t[1] - y) * abs(t[1] - y)) + (abs(t[0] - x) * abs(t[0] - x)))
        # answer.append(min(pre))

    return answer