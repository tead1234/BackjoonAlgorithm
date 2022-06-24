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

            if coniPlace >= d[i-1] * 2:
                d[i] = d[i-1] * 2

        if d[i-1] > coniPlace:
            d[i] = d[i-1] - 1

        if d[i] == coniPlace:
            return i
    return False
## mid시간을 찍어서 코니의 위치를 파악한후 브라운이 그 시간동안 도달할 수 씨는 최소 mid를 찾으면된다
def solution(start, placeConi, placeBrw):
    end =
    while(True):
        mid = (start + end) // 2
        pros = Coni(mid,placeConi) ## pros 코니가 주어진 mid에 가있는 거리
        ## 만약 코니가 300000이상으로 가있으면 mid를 줄여야됨
        if pros > 300000:
            end = mid -1
            solution(start,end,placeConi,placeBrw)
        elif Brw(placeBrw,pros) == mid:
            return mid
        ## 브라운 위치 찾기 mid시간에

        elif Brw(placeBrw,pros) < mid:
            end = mid-1
            solution(start, end,placeConi, placeBrw)

        elif Brw(placeBrw,pros) > mid:
            start = mid +1
            solution(start, end, placeConi, placeBrw)

        elif Brw(placeBrw,pros) == False:
            return -1



placeConi= int(input("코니"))
placeBrown = int(input("브라운"))

print(Brw(4,299927))
print(solution(0,2000,placeConi,placeBrown))
