from collections import deque
n,k = map(int,input().split())
pad = list(map(int,input().split()))
onRobot = deque(pad[:n])
N = 2*n-1
notRobot = deque(pad[N:n-1:-1])
numOf0 = 0 ## 이전단계, 현재 단계
robotList = deque([0] * n)
ans = 0
num =  0
while num < k:
    ## 벨트 회전
    ans += 1
    num = 0
    notRobot.append(onRobot.pop())
    onRobot.appendleft(notRobot.popleft())
    ## 로봇리스트도 이동시켜야됨
    v = robotList.pop()
    robotList.appendleft(v)
    ## 로봇 놓기
    robotList[0] = 1
    onRobot[0] -= 1
    ## 로봇 한걸음 이동, 발판이 없으면 못감, 앞 로봇이 못가면 얘도 못감
    ## 이동이 가능하면 발판 을 하나 줄임
    ## 아래는 돌리기 전에 n-1 자리에 있는 애를 뺀거고
    ## 돌리고 나서 n-1에 있는 애도빼줘야됨
    for i in range(n-1,-1, -1):
        if i == n-1 and robotList[i] == 1:
            robotList[i] = 0
            continue
        if robotList[i] ==1 and onRobot[i+1] > 0:
            if robotList[i+1] == 0:
                robotList[i+1] = 1
                robotList[i] = 0
                onRobot[i+1] -= 1
            if i == n-2 and robotList[i+1] == 1:
                robotList[i+1] = 0

    for x in onRobot:
        if x == 0:
            ## 계속더해지니깐 이렇게 찾아내면 안됨
            num += 1
    for y in notRobot:
        if y == 0:
            num += 1



print(ans)

    ### 이동한 곳의 발판 지우기

