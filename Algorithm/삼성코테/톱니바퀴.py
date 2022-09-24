wh1 = list(map(int,input()))
wh2 = list(map(int,input()))
wh3 = list(map(int,input()))
wh4 = list(map(int,input()))
WH = [wh1,wh2,wh3,wh4]
N = int(input())
changeList = [list(map(int,input().split())) for _ in range(N)]
# -1 이면 반시계 , 1이면 시계
# 마주보는 톱니바퀴에 대한 정보를 저장할 리스트
t = [(3,wh1[2]),(wh2[6],wh2[2]), (wh3[6],wh3[2]) , (wh4[6],3)]
changeED = []
# 변화과정을 기록
def check(num,dir):
    if (num,dir) not in changeED:
        changeED.append((num,dir))
        if num == 0:
            a,b = t[num]
            c,d = t[num+1]
            if b != c:
                check(num+1, dir * -1)
        elif num == 1:
            a, b = t[num]
            c, d = t[num + 1]
            w,k = t[num - 1]
            if b != c:
                check(num + 1, dir * -1)
            if a != k:
                check(num-1, dir * -1)
        elif num == 2:
            a, b = t[num]
            c, d = t[num + 1]
            w,k = t[num - 1]
            if b != c:
                check(num + 1, dir * -1)
            if a != k:
                check(num-1, dir * -1)
        elif num == 3:
            a, b = t[num]
            w,k = t[num - 1]
            if a != k:
                check(num-1, dir * -1)
def turnRight(A):
    first = A[0]
    for i in range(len(A)-1):
        A[i] = A[i+1]
    A[len(A)-1] = first
    return A
def turnLeft(A):
    last = A[len(A)-1]
    for i in range(len(A)-1,0,-1):
        A[i] = A[i-1]
    A[0] = last
    return A

for i in range(N):
    # tart에서 1뺴줘야 제대로 나옴
    target , dir = changeList[i]
    TARGET  = target -1
    # 주변에 바뀌어야할 애들 파악
    check(TARGET,dir)
    ## 바뀔애들하고 방향 목록
    for a in changeED:
        C,V = a
        if V == 1:
            WH[C] = turnLeft(WH[C])
        else:
            WH[C] =turnRight(WH[C])
    t = [(3, wh1[2]), (wh2[6], wh2[2]), (wh3[6], wh3[2]), (wh4[6], 3)]
    changeED = []
ans = 0
for w in range(4):
    if WH[w][0] == 1 and w == 0:
        ans+= 1
    if WH[w][0] == 1 and w == 1:
        ans+= 2
    if WH[w][0] == 1 and w == 2:
        ans+= 4
    if WH[w][0] == 1 and w == 3:
        ans+= 8
print(ans)