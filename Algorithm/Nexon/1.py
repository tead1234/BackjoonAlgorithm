def minNum(samDaily, kellyDaily, difference):
    # d = 날짜
    d = 0
    S = difference
    K = 0

    while S >= K:
        ## 탈출조건
        if (kellyDaily - samDaily) <= 0:
            return -1
            break
        d += 1
        S += samDaily
        K += kellyDaily
    return d

print(minNum(100,100,0))