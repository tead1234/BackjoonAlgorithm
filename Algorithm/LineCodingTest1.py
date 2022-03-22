##코니는 처음 위치 C에서 1초 후 1만큼 움직이고, 이후에는 가속이 붙어 매 초마다 이전 이동 거리 + 1만큼 움직인다. 즉 시간에 따른 코니의 위치는 C, C + 1, C + 3, C + 6, …이다.
## 코니 위치 구하는 함수 0 1 3 6
## y는 최초 위치
def Coni(x, start):
    d = [0] * 2001
    d[0] = start
    d[1] = start + 1
    for i in range(2, 2000):
        if i >= 1:
            d[i] = d[i - 1] + i
    return d[x]
## 브라운은 최대한 Coni와 가깝게 움직일거임 >> 즉 Coni의 위치에서 가장 가깝게 움직일거

def Brw(start,coniPlace):
    d = [0] * 1000001
    d[0] = start
    d[1] = 1 + start
    for i in range(2,1000001):
        if coniPlace >= d[i-1] + 1:
            d[i] = d[i - 1] + 1
            if d[i] == coniPlace:
                return d[i]
            if coniPlace >= d[i-1] * 2:
                d[i] = d[i-1] * 2
                if d[i] == coniPlace:
                    return d[i]
        else:
            d[i] = d[i-1] - 1
            if d[i] == coniPlace:
                return d[i]
    return False

def solution(start, end, placeConi, placeBrw):
    mid = (start + end) // 2
    while(True):
        pros = Coni(mid,placeConi)

        if Brw(placeBrw,pros) == mid:
            return mid
        ## 브라운 위치 찾기 mid시간에

        if Brw(placeBrw,pros) < mid:
            solution(start, mid-1,placeConi, placeBrw)

        if Brw(placeBrw,pros) > mid:
            solution(mid + 1, end, placeConi, placeBrw)

        if Brw(placeBrw,pros) == False:
            return -1



placeConi= int(input("코니"))
placeBrown = int(input("브라운"))


print(solution(0,2000,placeConi,placeBrown))
