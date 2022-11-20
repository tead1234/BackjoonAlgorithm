T = int(input())


## 그냥 완탐으로 풀까?
for test_case in range(1, T + 1):
    n,m = map(int,input().split())
    Map = list(map(int,input().split()))
    points = []
    for idx,m in enumerate(Map):
        if m == 1:
            points.append(idx)

    dic = {}
    def findMax(a, Map):
        # 왼쪽부터
        b = a
        c = a

        while Map[b] != -1 and b >= 0:
            b -= 1
        while c != len(Map) and c < len(Map):
            c += 1
        if b == -1 and c != len(Map):
            return c
        elif b != -1 and c == len(Map):
            return b
        elif b == -1 and c == len(Map):
            return False
        elif b != -1 and c != len(Map):
            if abs(a - b) > abs(c - a):
                return c
            elif abs(a - b) < abs(c - a):
                return b
            elif abs(a- b) != abs(c- a):
                return False
    for p in points:
        ma = Map.copy()
        ma[p] = 0
        while findMax(p,ma):
            p = findMax(p, ma)
            ma[p] = 0
            # if p == len(ma) or p == -1:
            #     break
        print(ma)

    # print("#{} {}".format(test_case, answer))